import asyncio
import websockets

async def handle_message(message):
    print('got message: {}'.format(message))

async def process_messages(websocket):
    async for message in websocket:
        await handle_message(message)

async def subscribe():
    uri = 'ws://localhost:8989'
    async with websockets.connect(uri) as websocket:
        await process_messages(websocket)

asyncio.get_event_loop().run_until_complete(subscribe())
