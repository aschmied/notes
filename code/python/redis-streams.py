"""
deploy redis:

helm install -n testing anthony-redis bitnami/redis

port forward from local:

kubectl port-forward -n testing svc/anthony-redis-master 6380:6379
kubectl port-forward -n testing svc/anthony-redis-replicas 6381:6379

or deploy pods to experiment with:

kubectl run -n testing anthony-redis-producer --image python:3.10 --command -- sleep infinity
kubectl run -n testing anthony-redis-consumer --image python:3.10 --command -- sleep infinity

kubectl exec --tty -i anthony-redis-producer --namespace testing -- bash
kubectl exec --tty -i anthony-redis-consumer --namespace testing -- bash

to copy up the code:

kubectl cp run.py testing/anthony-redis-producer:/
kubectl cp run.py testing/anthony-redis-consumer:/

to clean up:

kubectl delete pod -n testing anthony-redis-producer
kubectl delete pod -n testing anthony-redis-consumer
helm uninstall -n testing anthony-redis


Pipelines ref: https://github.com/redis/redis-py#pipelines
"""

import logging
import sys
import time

import redis

_PASSWORD = "your-password"
_REDIS_GET_ALL_MESSAGES_ID = "0-0"
_REDIS_USE_DEFAULT_ID = "*"
_BATCH_SIZE = 1  # 2K msgs/sec
# _BATCH_SIZE = 10  # 17K msgs/sec
# _BATCH_SIZE = 100  # 48K msgs/sec
# _BATCH_SIZE = 1000  # 60K msgs/sec


def build_client(host: str, port: int) -> redis.Redis:
    return redis.Redis(host=host, port=port, password=_PASSWORD)


class Producer:
    def __init__(self, client: redis.Redis, stream_name: str) -> None:
        self._client = client.pipeline()
        self._stream_name = stream_name
        self._message_count_batch = 0
        self._message_count = 0
        self._byte_count = 0
        self._last_log_time = 0
        self._start_time = time.monotonic()

    def write(self, message: str) -> None:
        fields = {"content": message}
        self._client.xadd(
            self._stream_name,
            fields,
            id=_REDIS_USE_DEFAULT_ID,
            maxlen=10000,
            approximate=True,
        )
        self._message_count_batch += 1
        self._message_count += 1
        self._byte_count += len(message)
        self._commit()
        self._log()

    def _commit(self):
        if self._message_count_batch < _BATCH_SIZE:
            return
        self._client.execute()
        self._message_count_batch = 0

    def _log(self):
        now = time.monotonic()
        if now - self._last_log_time < 5.0:
            return
        duration = now - self._start_time
        msg_count = self._message_count
        byte_count = self._byte_count
        logging.info(
            "Wrote %s messages, %s bytes. Avg %s msg/sec, %s bytes/sec",
            msg_count,
            byte_count,
            msg_count / duration,
            byte_count / duration,
        )
        self._last_log_time = now


class Consumer:
    """
    Probably want to use hiredis parser: https://github.com/redis/redis-py#parsers.
    """

    def __init__(self, client: redis.Redis, stream_name: str) -> None:
        self._client = client
        self._stream_name = stream_name
        self._last_processed_id = _REDIS_GET_ALL_MESSAGES_ID
        self._message_count = 0
        self._byte_count = 0
        self._last_log_time = 0
        self._start_time = time.monotonic()

    def read(self) -> None:
        # [[b'test', [(b'1637884307322-0', {b'message_type': b'refresh', b'content': b'"{\\"type\\": \\"refresh\\"}"'})]]]
        while True:
            response = self._client.xread(
                {self._stream_name: self._last_processed_id},
                count=_BATCH_SIZE,
                block=1000,
            )
            if len(response) == 0:
                continue
            this_stream_respone = response[0]
            stream_id, messages = this_stream_respone
            assert stream_id.decode("utf-8") == self._stream_name
            if len(messages) == 0:
                continue
            for message in messages:
                message_id, fields = message
                self._last_processed_id = message_id.decode("utf-8")
                message = fields[b"content"]
                decoded_message = message.decode("utf-8")
                self._message_count += 1
                self._byte_count += len(decoded_message)
                yield decoded_message
                self._log()

    def _log(self):
        now = time.monotonic()
        if now - self._last_log_time < 5.0:
            return
        duration = now - self._start_time
        msg_count = self._message_count
        byte_count = self._byte_count
        logging.info(
            "Read %s messages, %s bytes. Avg %s msg/sec, %s bytes/sec",
            msg_count,
            byte_count,
            msg_count / duration,
            byte_count / duration,
        )
        self._last_log_time = now


def read_messages():
    with open("messages.ndjson") as f:
        lines = f.readlines()
        logging.info("Read %s messages from disk", len(lines))
        return lines


def run_producer():
    client = build_client("anthony-redis-master.testing.svc.cluster.local", 6379)
    producer = Producer(client, "summarycalc-message-stream")
    messages = read_messages()
    while True:
        for message in messages:
            producer.write(message)


def run_consumer():
    client = build_client("anthony-redis-replicas.testing.svc.cluster.local", 6379)
    consumer = Consumer(client, "summarycalc-message-stream")
    for message in consumer.read():
        pass


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    if sys.argv[1] == "p":
        run_producer()
    elif sys.argv[1] == "c":
        run_consumer()
    logging.error("Provide arg p or c.")
