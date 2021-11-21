# Redis Streams


## High-level

* Indexed by time and sequence number
* List of serialized fields + radix tree
* Supports requests by index ranges
* Note sequence numbers are `<epoch-millisecond>-<sequence-num>`. Multiple messages received in the same epoch millisecond receive sequentially incrementing sequence numbers. Both of these are 64-bit unsigned integers

## Usage pattern for queue-like behaviour

* Messages are added with `XADD`
* Client does a blocking read with 5 second timeout on streams `mystream` and `other stream`. `$ $` is the sequence number range and means "assume I already have all the existing messages"

        XREAD BLOCK 5000 STREAMS mystream otherstream $ $

    If this returns the message

        "otherstream" 1506935385635-0 "message" "Hi There"

    Then we can use that sequence number as the starting point for the next blocking read

        XREAD BLOCK 5000 STREAMS mystream otherstream $ 1506935385635-0

* Always use the `COUNT` option to limit the number of results in case of reconnecting after downtime
* The stream max size is provided on the `XADD`. You can specify a hard max like

        XADD mystream MAXLEN 1000000 * foo bar

    but this means you pay for list trimming on the the add. Instead, you can specify a "soft" max to only remove entire blocks. This makes the cleanup nearly free:

        XADD mystream MAXLEN ~ 1000000 * foo bar

* There is a concept of "consumer groups" for scaling workloads: each messages is processed by one consumer in the group
* Consumer groups provides an "at least once" guarantee with messages being resent after an ACK timeout
* The representation is memory efficient and fast to persist and replicate
* The feature was developed in Redis 4.2, but seems to only be available from 5.0 ([ref](https://redis.io/topics/streams-intro))

## Persistence

* Streams and consumer group states are replicated and persisted in AOF and RDB files
* There are limitations and potential data loss in failover events. See the [Persistence, replication and message safety](https://redis.io/topics/streams-intro) section of the Streams Intro for a brief introduction. See the [Cluster tutorial](https://redis.io/topics/cluster-tutorial) for details

## Reference

* This is all based on the `<antirez>` [blog post on Redis Streams](http://antirez.com/news/114)
* A more indepth introduction is given in the [streams intro doc](https://redis.io/topics/streams-intro)
