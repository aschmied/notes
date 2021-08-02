# From https://www.tornadoweb.org/en/stable/websocket.html#client-side-support

import asyncio
import datetime
import time
import tornado.websocket

async def main():
    # Use wss:// for secure websockets connections.
    url = 'ws://localhost:8888'
    #url = 'wss://aschmied-test.nmx.ca'
    conn = await tornado.websocket.websocket_connect(url)
    while True:
        reply = await conn.read_message()
        if reply is None:
            print('{}: Server closed the connection'.format(datetime.datetime.now()))
            break
        print('{}: {}'.format(datetime.datetime.now(), reply))

if __name__ == '__main__':
    print('{}: starting'.format(datetime.datetime.now()))
    asyncio.get_event_loop().run_until_complete(main())
