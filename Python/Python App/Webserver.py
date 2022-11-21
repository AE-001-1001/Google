from http.server import BaseHTTPRequestHandler, HTTPServer
from App import *
import time

hostName = "localhost"
serverPort = 8080

class MyServerCums(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Title goes here.</title></head>", "utf-8"))
        #print the time with auto refresh
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Current time is: %s</p>" % time.asctime(), "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        self.wfile.write(bytes("<p>You accessed path: %s</p>" % self.path, "utf-8"))
        self.wfile.write(bytes("<p>Example of a Webserver through python!</p>", "utf-8"))
        self.wfile.write(bytes("</body></html>", "utf-8"))
    


def main():
    webserver = HTTPServer((hostName, serverPort), MyServerCums)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webserver.serve_forever()
    except KeyboardInterrupt:
        pass

    webserver.server_close()
    print("Server stopped.")
    return 