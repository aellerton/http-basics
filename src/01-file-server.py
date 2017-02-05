import http.server
import os
import socketserver

if __name__ == "__main__":
    root_dir = os.getcwd()
    port = 8001
    server_address = ("", port)
    handler = http.server.SimpleHTTPRequestHandler

    print("httpd serving files from %s on port %d" % (root_dir, port))

    httpd = socketserver.TCPServer(server_address, handler)
    httpd.serve_forever()
