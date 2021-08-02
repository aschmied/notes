import zmq

def main():
    context = zmq.Context()
    print('connecting...')
    socket = context.socket(zmq.SUB)
    socket.connect('tcp://localhost:8989')
    print('connected. starting receive loop')

    socket.setsockopt_string(zmq.SUBSCRIBE, '')
    while True:
        message_content = socket.recv_string()
        print('got message: {}'.format(message_content))

if __name__ == '__main__':
    main()
