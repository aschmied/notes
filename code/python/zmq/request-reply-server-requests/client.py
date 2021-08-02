import zmq
import signal


def main():
    signal.signal(signal.SIGINT, signal.SIG_DFL);

    context = zmq.Context()
    print('connecting...')
    socket = context.socket(zmq.REP)
    # socket.setsockopt(zmq.SNDTIMEO, 5000)
    # socket.setsockopt(zmq.RCVTIMEO, 5000)
    socket.connect('ws://localhost:8989')
    print('connected')

    while True:
        request = socket.recv_string(0)
        print('Got request: {}'.format(request))
        socket.send_string('reply')

if __name__ == '__main__':
    main()
