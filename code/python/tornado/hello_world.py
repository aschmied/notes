# Example from https://github.com/tornadoweb/tornado#hello-world

import tornado.ioloop
import tornado.web

class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write("Hello world")

def build_app():
    return tornado.web.Application([
        (r'/', MainHandler)
    ])

if __name__ == '__main__':
    app = build_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
