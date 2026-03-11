from http.server import BaseHTTPRequestHandler, HTTPServer
import json , os , socket , time

PORT = 8080
ENV = "development"
START_TIME= time.time()

def make_html(count):
    uptime = time.time() - START_TIME
    return f"""<!DOCTYPE html>
<html lang="en">
<title>IBM cloud Service </title>
<style></style>
<body>
<div class="card">
    <h1>Hello !!! IBM Cloud </h1>
    <p>Request count: {count}</p>
    <p>Uptime: {uptime:.2f} seconds</p>
    <p>Hostname: {socket.gethostname()}</p>
    <p>Environment: {ENV}</p>
    <p>uptime: {uptime:.2f} seconds</p>

</div>

</body>
</html>"""