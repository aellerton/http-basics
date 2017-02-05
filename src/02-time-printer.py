import http.server
import os
import socketserver
import time

from http import HTTPStatus


class TimePrinter(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        t = time.gmtime()
        s = "Time for '%s': %s" % (self.path, time.strftime("%c", t))

        # Uncomment this to see the headers of the request
        #print("headers", self.headers)

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", len(s))
        self.end_headers()
        self.wfile.write(str.encode(s))


if __name__ == "__main__":
    port = 8001
    server_address = ("", port)
    handler = TimePrinter

    print("httpd serving time on port %d" % (port,))

    httpd = socketserver.TCPServer(server_address, handler)
    httpd.serve_forever()
