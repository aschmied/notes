import zmq

def main():
    context = zmq.Context()
    print('connecting...')
    socket = context.socket(zmq.REQ)
    socket.connect('tcp://localhost:8989')
    print('connected')

    socket.send_string("hello")
    reply = socket.recv_string()
    print('got reply: {}'.format(reply))

if __name__ == '__main__':
    main()
