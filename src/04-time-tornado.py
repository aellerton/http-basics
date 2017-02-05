from http import HTTPStatus

import arrow
import handy
import tornado.ioloop
import tornado.web


class TimeHandler(tornado.web.RequestHandler):
    def get(self):
        t = arrow.utcnow()
        tz = self.get_argument('tz', None)
        if not tz or not tz.strip():
            tz = 'local'

        try:
            t = t.to(tz)
        except arrow.parser.ParserError as e:
            raise tornado.web.HTTPError(HTTPStatus.BAD_REQUEST[0], "Bad timezone '%s': %s" % (tz, e))

        s = "%s (%s)" % (t.format(), tz)
        self.write(s)


class HelloHandler(tornado.web.RequestHandler):
    def get(self):
        name = self.get_argument('name', None)
        if not name or not name.strip():
            name = 'World'
        self.write("Hello, %s" % name)


def make_app():
    return tornado.web.Application([
        (r"/", TimeHandler),
        (r"/hello", HelloHandler),
    ])


if __name__ == "__main__":
    # addr = handy.pop_arg_str() or ""
    port = handy.pop_arg_int() or 8000

    app = make_app()
    app.listen(port)
    print("Time Tornado HTTPD on port %d" % port)
    tornado.ioloop.IOLoop.current().start()
