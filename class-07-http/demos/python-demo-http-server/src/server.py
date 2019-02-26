from http.server import HTTPServer, BaseHTTPRequestHandler

class SimpleRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(b'<html><body><h1>Any GET, any url</h1></body></html>')
        return

def run_forever():
    port = 5000
    server_address = ('', port)
    server = HTTPServer(server_address, SimpleRequestHandler)

    try:
        server.serve_forever()

    except KeyboardInterrupt:
        server.server_close()
        server.shutdown()
       

if __name__ == "__main__":
    run_forever()