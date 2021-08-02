import http.server
import json
import logging

def main():
    logging.basicConfig(level=logging.INFO)
    port = 8123
    address = ('', port)
    server = http.server.HTTPServer(address, HTTPRequestHandler)
    logging.info('Starting HTTP server')
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
    logging.info('Terminating HTTP server')
    server.server_close()

class HTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info(f'GET {self.path}\n{self.headers}')
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()
        self.wfile.write(self._response_content())

    def _response_content(self):
        return json.dumps({
            'foo': 'zzz'
            }).encode('utf-8')


if __name__ == '__main__':
    main()
