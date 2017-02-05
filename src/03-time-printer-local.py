import http.server
import socketserver
from http import HTTPStatus

import arrow

import handy


class TimePrinter(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        path, args = handy.parse_path(self.path)
        t = arrow.utcnow()
        tz = args.get('tz') or 'local'

        try:
            t = t.to(tz)
        except arrow.parser.ParserError as e:
            self.send_error(HTTPStatus.BAD_REQUEST, "Bad timezone '%s': %s" % (tz, e))
            return

        s = "Request is for %s\nPath=%s\nQuery string params=%s\nTime=%s (%s)" % (self.path, path, args, t.format(), tz)

        self.send_response(HTTPStatus.OK)
        self.send_header("Content-type", "text/plain")
        self.send_header("Content-Length", len(s))
        self.end_headers()
        self.wfile.write(str.encode(s))


if __name__ == "__main__":
    addr = handy.pop_arg_str() or ""
    port = handy.pop_arg_int() or 8001
    handler = TimePrinter

    print("httpd serving time %s:%d (use ?tz=local|UTC|US/Eastern etc)" % (addr, port))

    httpd = socketserver.TCPServer((addr, port), handler)
    httpd.serve_forever()
