This example implements a pubsub pattern. It is based on the examples [here](https://websockets.readthedocs.io/en/stable/intro.html#common-patterns).

To use:

    pip install websockets
    python broker.py &
    python publisher.py &
    python subscriber.py &
    python subscriber.py

The broker listens on two ports: one for subscribers and one for the publisher. The publisher sends a request to the broker and waits for a reply every 5 seconds. Clients receive messages from the broker. The broker forwards messages from the publisher to the subscribers. All websockets are long-lived in this example.

Tested with Python 3.7.
