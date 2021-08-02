import asyncio
from autobahn.asyncio.wamp import ApplicationSession, ApplicationRunner

class Component(ApplicationSession):
    async def on_join(self, details):
        print('Session attached')
        topic = 'com.myapp.topic1'
        counter = 0
        while True:
            print('Publishing to {}'.format(topic))
            self.publish(topic, 'Hello {}'.format(counter))
            counter += 1
            await asynchio.sleep(1)

if __name__ == '__main__':
    url = 'ws://localhost:9000/ws'
    realm = 'crossbardemo'
    runner = ApplicationRunner(url, realm)
    runner.run(Component)
