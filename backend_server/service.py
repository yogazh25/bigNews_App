import pyjsonrpc
import json

SERVER_HOST='localhost'
SERVER_PORT = 4040

class RequestHandler(pyjsonrpc.HttpRequestHandler):
    """test method for pyjsonrpc."""
    @pyjsonrpc.rpcmethod
    def add(self, a, b):
        print "Add %d and %d" % (a, b)
        return a + b


http_server = pyjsonrpc.ThreadingHttpServer(
    server_address = (SERVER_HOST, SERVER_PORT),
    RequestHandlerClass = RequestHandler
)

print "Starting HTTP server on %s:%d" % (SERVER_HOST, SERVER_PORT)

http_server.serve_forever()
