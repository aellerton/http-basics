# Learning HTTP Fundamentals

Some notes and code for learning the basics of how HTTP works.

Won't make much sense without an instructor.

## Run Notes

Run:

    $ telnet devd.io 8000
    Trying 127.0.0.1...
    Connected to devd.io.
    Escape character is '^]'.
    GET /foo.html HTTP/1.1
    host: devd.io:8000

Note that the protocol version ("HTTP/1.1") *must* be present,
and that the host header *must* be present.


Then:
    http devd.io:8000/hello.txt
    http devd.io:8000/foo.html



Use nc with ``-c``:

"""
nc -c 127.0.0.1 8000   # The "-c" is VERY important for CRLF!
GET / HTTP/1.0
Host: 127.0.0.1:8000

"""

To monitor traffic:

    sudo tcpflow -p -c -i lo0 port 8000


To hex dump, add "-D":

    sudo tcpflow -p -c -i lo0 -D port 8000


The Python Tornado example:

    python src/04-time-tornado.py

Show results with:

    http localhost:8000/hello
    http localhost:8000/hello\?name=Andrew
    http localhost:8000/      # get current time
    http localhost:8000/?tz=  # same as not giving any tz arg
    http localhost:8000/?tz=local
    http localhost:8000/?tz=UTC
    http localhost:8000/?tz=Australia/Sydney
    http localhost:8000/?tz=EST
    http localhost:8000/?tz=Australia/Perth

