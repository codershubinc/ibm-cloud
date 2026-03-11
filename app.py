from http.server import BaseHTTPRequestHandler, HTTPServer
import json , os 

services = [
    {
        "name": "IBM Watson Assistant",
        "description": "It is a powerful AI service that allows you to build conversational interfaces and chatbots.",
        "endpoint": "/service1"
    },
    {
        "name": "Service 2",
        "description": "This is the second service.",
        "endpoint": "/service2"
    },
    {
        "name": "Service 3",
        "description": "This is the third service.",
        "endpoint": "/service3"
    }
]

def build_rows():
    rows = ""
    for service in services:
        free_html= f"<span style='color: green; font-weight: bold;'>Free</span>"  
        rows += f"<tr><td>{service['name']}</td><td>{service['description']}</td><td><a href='{service['endpoint']}'>Access</a> </td> <td>{free_html} </td> </tr>"
    return rows

html = f"""<!DOCTYPE html>
<html lang="en"> 
    <style> 
    </style>
    <body>
        <h1>Available Services</h1>
        <table border="1">
            <tr>
                <th>Name</th>
                <th>Description</th>
                <th>Endpoint</th>
                <th>Cost</th>
            </tr>
            {build_rows()}
        </table>
    </body>
</html>
"""

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(html.encode('utf-8'))

    def log_message(self, format, *args):
        return

print("Starting server on port http://localhost:8080...")
PORT = 8080

HTTPServer(('', PORT), MyHandler).serve_forever()