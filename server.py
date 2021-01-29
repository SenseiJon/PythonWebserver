import http.server
import socketserver

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print("Instructor Jon's amazing server is now running at port:", PORT)
    httpd.serve_forever()
