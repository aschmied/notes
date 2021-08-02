# From https://github.com/crossbario/autobahn-python/tree/master/examples/asyncio/websocket

import asyncio
from autobahn.asyncio.websocket import WebSocketClientFactory
from autobahn.asyncio.websocket import WebSocketClientProtocol

class MyClientProtocol(WebSocketClientProtocol):

    def onConnect(self, response):
        print('Connecting: {}'.format(response.peer))

    def onConnecting(self, transport_details):
        print('Connecting: {}'.format(transport_details))

    def onOpen(self):
        print('WebSocket connection open.')

        def hello():
            self.sendMessage('Hello, world!'.encode('utf8'))
            self.factory.loop.call_later(1, hello)

        # Send a message every second.
        hello()

    def onMessage(self, payload, isBinary):
        if isBinary:
            print('Binary message received: {} bytes'.format(len(payload)))
        else:
            print('Text message received: {}'.format(payload.decode('utf8')))


    def onClose(self, wasClean, code, reason):
        print('WebSocket connection closed: {}'.format(reason))

if __name__ == '__main__':
   factory = WebSocketClientFactory('ws://localhost:9000')
   factory.protocol = MyClientProtocol

   loop = asyncio.get_event_loop()
   coro = loop.create_connection(factory, 'localhost', 9000)
   loop.run_until_complete(coro)
   loop.run_forever()
   loop.close()
