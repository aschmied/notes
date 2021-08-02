import signal
import time
import zmq

def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL);

    context = zmq.Context()
    print('binding')
    socket = context.socket(zmq.REQ)
    # Docs: http://api.zeromq.org/3-2:zmq-setsockopt
    socket.setsockopt(zmq.SNDTIMEO, 5000)
    socket.setsockopt(zmq.RCVTIMEO, 5000)
    print('timeo is {}'.format(socket.getsockopt(zmq.RCVTIMEO)))
    socket.bind('ws://*:8989')
    print('bound. starting request')
    while True:
        try:
            socket.send_string('message')
        except zmq.error.Again:
            print('Timed out on send')
        print('sent')

        try:
            reply = socket.recv_string(0)
        except zmq.error.Again:
            print('Timed out on recv')
        print('received reply: {}'.format(reply))

        time.sleep(5)


if __name__ == '__main__':
    main()
