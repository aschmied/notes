This example implements a request-reply pattern. It is based on the examples [here](https://websockets.readthedocs.io/en/stable/intro.html#common-patterns).

To use:

    pip install websockets
    python server.py &
    python client.py

The client script sends a request, waits for a reply and exits. The websocket lives only for the duration of the request/reply in this case.

Tested with Python 3.7.
