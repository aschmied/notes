# Example from https://www.tornadoweb.org/en/stable/websocket.html

import tornado.websocket

# You get an instance of this class per connected client.
class EchoWebSocketHandler(tornado.websocket.WebSocketHandler):
    def open(self):
        print('Websocket opened')

    def on_message(self, message):
        self.write_message(u'Reply from {}: {}'.format(id(self), message))

    def on_close(self):
        print('Websocket closed')

def build_app():
    return tornado.web.Application([
        (r'/', EchoWebSocketHandler)
    ])

if __name__ == '__main__':
    app = build_app()
    app.listen(8888)

    # This blocks.
    tornado.ioloop.IOLoop.current().start()
