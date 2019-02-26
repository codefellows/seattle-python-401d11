from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
import os


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed_path = urlparse(self.path)
        parsed_qs = parse_qs(parsed_path.query)

        if parsed_path.path == '/':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'<html><body><h1>hi!</h1></body></html>')
            return

        elif parsed_path.path == '/test':
            try:
                cat = parsed_qs['category'][0]
            except KeyError:
                self.send_response_only(400)
                self.end_headers()
                return

            self.send_response(200)
            self.end_headers()
            self.wfile.write(b'we did the thing with the qs')
            return

        self.send_response_only(404)
        self.end_headers()

    def do_HEAD(self):
        self.send_response(302)
        self.send_header('Content-type', 'text/plain')
        self.end_headers()

    def do_POST(self):
        # NOTE: Doesn't do anything with posted data
        self.send_response_only(201)
        self.end_headers()
        self.wfile.write(b'<html><body><h1>POST!</h1></body></html>')


def run_forever():

    port = int(os.environ['PORT'] or 5000)

    server_address = ('localhost', port)
    
    server = HTTPServer(server_address, SimpleHTTPRequestHandler)

    try:
        print(f'Starting server on port {port}')
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()


if __name__ == '__main__':
    run_forever()
