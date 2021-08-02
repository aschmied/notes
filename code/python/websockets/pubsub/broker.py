import asyncio
import time
import websockets

subscriptions = set()

async def handle_subscriber(websocket, path):
    await connect_subscriber(websocket)
    try:
        await websocket.wait_closed()
    except websockets.exceptions.ConnectionClosedOK:
        pass
    finally:
        await disconnect(websocket)

async def connect_subscriber(websocket):
    print('connected')
    subscriptions.add(websocket)

async def disconnect_subscriber(websocket):
    print('disconnected')
    subscriptions.remove(websocket)

async def handle_publisher(websocket, path):
    while True:
        message_content = await websocket.recv()
        response_content = 'OK: "{}"'.format(message_content)
        try:
            if not subscriptions:
                print('message dropped due to no subscribers')
            else:
                await asyncio.wait([asyncio.create_task(ws.send(message_content)) for ws in subscriptions])
        except websockets.exceptions.ConnectionClosed:
            print('connection closed during write for {}:{}'.format(websocket.host, websocket.port))
            pass
        await websocket.send(response_content)

subscriber_server = websockets.serve(handle_subscriber, 'localhost', 8989)
publisher_server = websockets.serve(handle_publisher, 'localhost', 8990)
asyncio.get_event_loop().run_until_complete(subscriber_server)
asyncio.get_event_loop().run_until_complete(publisher_server)

try:
    asyncio.get_event_loop().run_forever()
except KeyboardInterrupt:
    pass
