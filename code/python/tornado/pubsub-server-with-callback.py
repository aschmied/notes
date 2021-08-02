# Example from:
#   https://www.tornadoweb.org/en/stable/websocket.html
#   https://stackoverflow.com/a/18532575

import threading
import time
import tornado.websocket

# You get an instance of this class per connected client.
class EchoWebSocketHandler(tornado.websocket.WebSocketHandler):
    _handlers = set()

    def open(self):
        print('Websocket opened')
        self._handlers.add(self)

    def on_message(self, message):
        # Maybe an error in the logs?
        pass

    def on_close(self):
        print('Websocket closed')
        self._handlers.remove(self)

    @classmethod
    def publish(cls, callback, message):
        for index, handler in enumerate(cls._handlers):
            handler.write_message(message)
            callback('wrote message {}'.format(index))

def build_app():
    return tornado.web.Application([
        (r'/', EchoWebSocketHandler)
    ])

def publisher(io_loop):
    callback = lambda message: print('Received callback: {}'.format(message))
    # Docs: https://www.tornadoweb.org/en/stable/ioloop.html#callbacks-and-timeouts
    while True:
        io_loop.add_callback(lambda: EchoWebSocketHandler.publish(callback, 'hello everyone'))
        time.sleep(1)

if __name__ == '__main__':
    app = build_app()
    app.listen(8888)

    io_loop = tornado.ioloop.IOLoop.current()
    thread = threading.Thread(target=publisher, args=(io_loop,), daemon=True)
    thread.start()
    io_loop.start()
