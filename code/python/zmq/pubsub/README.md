This example implements a pub-sub pattern. It is illustrated in the ZMQ docs [here](http://zguide.zeromq.org/page:chapter2#The-Dynamic-Discovery-Problem). Documentation for setsockopt is [here](http://api.zeromq.org/master:zmq-setsockopt).

To use:

    pip install pyzmq
    python publisher.py &
    python subscriber.py &
    python subscriber.py

Tested with Python 3.7.
