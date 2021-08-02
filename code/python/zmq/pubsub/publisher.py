import time
import zmq

def main():
    context = zmq.Context()
    print('binding')
    socket = context.socket(zmq.PUB)
    socket.bind('tcp://*:8989')
    print('bound. starting publish loop')
    while True:
        message_content = 'hello'
        print('publishing {}'.format(message_content))
        socket.send_string(message_content)
        time.sleep(5)

if __name__ == '__main__':
    main()
