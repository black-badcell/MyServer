from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs
from func import getAngle, getDefinedAngle
PORT = 8080


class myHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/getAngle":
            my_message = getAngle()
        elif self.path.startswith("/getDefinedAngle"):
            query_components = parse_qs(urlparse(self.path).query)
            time = query_components["time"][0]
            
            my_message = getDefinedAngle(time)
       


        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()

        self.wfile.write(str(my_message).encode("utf-8"))


server = HTTPServer(("", PORT), myHandler)
print("Started httpserver on port ", PORT)
server.serve_forever()
