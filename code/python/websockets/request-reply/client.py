import asyncio
import websockets

async def hello():
    uri = 'ws://localhost:8989'
    async with websockets.connect(uri) as websocket:
        await websocket.send('hello')
        reply = await websocket.recv()
        print('got reploy: {}'.format(reply))

asyncio.get_event_loop().run_until_complete(hello())
