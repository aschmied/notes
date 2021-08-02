# From https://www.tornadoweb.org/en/stable/websocket.html#client-side-support

import asyncio
import time
import tornado.websocket

async def main():
    # Use wss:// for secure websockets connections.
    conn = await tornado.websocket.websocket_connect('ws://localhost:8888')
    while True:
        request = 'my message'
        await conn.write_message(request)
        reply = await conn.read_message()
        if reply is None:
            print('Server closed the connection')
            break
        print(reply)
        time.sleep(1)

if __name__ == '__main__':
    asyncio.get_event_loop().run_until_complete(main())
