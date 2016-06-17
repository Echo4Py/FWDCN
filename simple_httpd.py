
from http.server import HTTPServer, CGIHTTPRequestHandler

port = 2016

httpd = HTTPServer(('', port), CGIHTTPRequestHandler)
print("Starting simple_httpd on port: " + str(httpd.server_port))
httpd.serve_forever()

