import asyncio
import websockets

async def subscribe():
    uri = 'ws://localhost:8990'
    async with websockets.connect(uri) as websocket:
        await publish_messages(websocket)

async def publish_messages(websocket):
    while True:
        response = await publish_message(websocket)
        print('got response: {}'.format(response))
        await asyncio.sleep(5)

async def publish_message(websocket):
    await websocket.send('hello')
    return await websocket.recv()

asyncio.get_event_loop().run_until_complete(subscribe())
