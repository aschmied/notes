import threading
import time

from obspy.clients.seedlink.easyseedlink import EasySeedLinkClient, create_client
from obspy.clients.seedlink.seedlinkexception import SeedLinkException

STREAMING_DURATION = 15


class SeedLinkClient(EasySeedLinkClient):
    # https://docs.obspy.org/packages/autogen/obspy.clients.seedlink.easyseedlink.html#module-obspy.clients.seedlink.easyseedlink
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._clear_retry_state()
        self._server_downtime_tolerance_seconds = 10
        self._max_retry_delay = 120
 
    def on_data(self, trace):
        self._clear_retry_state()
        print('---- Recv ----')
        print(trace)

    def _clear_retry_state(self):
        self._retry_delay = 4
        self._last_packet_time = time.monotonic()

    def _server_down_too_long(self):
        return self._time_since_successful_packet() > self._server_downtime_tolerance_seconds

    def _time_since_successful_packet(self):
        return time.monotonic() - self._last_packet_time

    def on_seedlink_error(self):
        # https://docs.obspy.org/packages/autogen/obspy.clients.seedlink.easyseedlink.EasySeedLinkClient.on_seedlink_error.html#obspy.clients.seedlink.easyseedlink.EasySeedLinkClient.on_seedlink_error
        print('Received ERROR response')

    def on_terminate(self):
        # https://docs.obspy.org/packages/autogen/obspy.clients.seedlink.easyseedlink.EasySeedLinkClient.on_terminate.html#obspy.clients.seedlink.easyseedlink.EasySeedLinkClient.on_terminate
        print('Terminate')

    def stop(self):
        self.conn.terminate()

    def run_with_reconnect(self):
        while True:
            self._try_run()
            is_error = self._server_down_too_long()
            print('*** SeedLink client disconnected. Error: {}. Trying again in {} seconds'.format(is_error, self._retry_delay))
            time.sleep(self._retry_delay)
            self._retry_delay = min([self._retry_delay * 2, self._max_retry_delay])

    def _try_run(self):
        try:
            self.run()
        except (SeedLinkException, ConnectionResetError) as e:
            is_error = self._server_down_too_long()
            print('{}: {}'.format(type(e).__name__, is_error))

def main():
    # host = 'rtserve.iris.washington.edu'
    # port = '18000'
    host = '34.210.22.140'
    port = 18111
    # port = 18006
    url = f'{host}:{port}'

    print(f'Creating client for {url}')
    client = SeedLinkClient(url, autoconnect=False)
    print(f'Connecting')
    client.connect()

    print(f'Created SeedLink server at {url}')
    get_and_print_info = lambda key: print(f'{key}: {client.get_info(key)}')
    get_and_print_info('ID')
    get_and_print_info('CAPABILITIES')
    # get_and_print_info('STATIONS')
    # get_and_print_info('STREAMS')
    # get_and_print_info('GAPS')
    # get_and_print_info('CONNECTIONS')
    # get_and_print_info('ALL')
    print(f'Capabilities attribute: {client.capabilities}')
    # client.select_stream(net='1E', station='MONT7', selector='HHE')
    client.select_stream(net='DS', station='DSA01', selector='HHZ')

    print('About to run')
    client.run_with_reconnect()
    # thread = threading.Thread(target=client.run)
    # thread.start()
    # print(f'Running for {STREAMING_DURATION} seconds...')

    # time.sleep(STREAMING_DURATION)

    # print('About to close...')
    # client.stop()
    # https://docs.obspy.org/packages/autogen/obspy.clients.seedlink.easyseedlink.EasySeedLinkClient.close.html#obspy.clients.seedlink.easyseedlink.EasySeedLinkClient.close
    print('Closed')

if __name__ == '__main__':
    main()
