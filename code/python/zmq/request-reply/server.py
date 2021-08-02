import zmq

def main():
    context = zmq.Context()
    print('binding')
    socket = context.socket(zmq.REP)
    socket.bind('tcp://*:8989')
    print('bound. starting request reply loop')
    while True:
        message_content = socket.recv_string(0)
        print('received message: {}'.format(message_content))
        response_content = 'received: "{}"'.format(message_content)
        socket.send_string(response_content)

if __name__ == '__main__':
    main()
