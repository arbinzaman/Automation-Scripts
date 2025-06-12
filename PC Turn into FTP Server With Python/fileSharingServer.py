import http.server
import socketserver
import os
import socket  # <-- Add this!

PORT = 8000
DIRECTORY = "F:/"  # <-- Set this to your folder path

os.chdir(DIRECTORY)

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), handler) as httpd:
    print(f"Serving at http://{os.getenv('COMPUTERNAME')} (port {PORT})")
    print(f"Access via: http://{socket.gethostbyname(socket.gethostname())}:{PORT}")
    httpd.serve_forever()
