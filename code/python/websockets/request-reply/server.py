import asyncio
import websockets

async def hello(websocket, path):
    message_content = await websocket.recv()
    response_content = 'received: "{}"'.format(message_content)
    print(response_content)
    await websocket.send(response_content)

start_server = websockets.serve(hello, 'localhost', 8989)
asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
