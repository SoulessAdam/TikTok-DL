from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import json
from requests import post

hostName = socket.gethostbyname(socket.gethostname())
serverPort = 8080

def grabDownloadUrl(url): # Grab download link from lovetik api
    apiUrl = "https://lovetik.com/api/ajax/search"

    req = post(apiUrl,
    data = {
            "query": url
    },
    headers = {
        "Origin": 'https://lovetik.com/',
        "Referer": 'https://lovetik.com/',
    })

    return req.json()["links"][0]["a"]

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self): # Serve web page with instructions
        self.send_response(400)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(bytes("<html><head><title>Error</title></head>", "utf-8"))
        self.wfile.write(bytes("<h1>GET Request: %s</h1>" % self.path, "utf-8"))
        self.wfile.write(bytes("<body>", "utf-8"))
        self.wfile.write(bytes("<p>Please use POST to request a download.</p>", "utf-8"))
        self.wfile.write("<p>The POST request should include TikTok URL using JSON with the key being \"url\".<br>Returned information is returned in JSON format...</p>".encode('utf-8'))
        self.wfile.write(bytes("</body></html>", "utf-8"))
        return

    def do_POST(self): # Send link back to webclient.
        content_length = int(self.headers.get('content-length', 0))
        post_data = json.loads(self.rfile.read(content_length))
        response = dict()
        if "url" not in post_data:
            self.send_response(400)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            response["error"] = "No URL.\nURL expected to download. Are you fucking stupid?"
        else:
            tiktok_url = post_data["url"]
            download_url = grabDownloadUrl(tiktok_url)
            if download_url is None:
                self.send_response(400)
                self.send_header("Content-type", "application/json")
                self.end_headers()
                response["error"] = "Problem with grabbing download link. Please check TikTok Link or try again."
            else:
                response["url"] = download_url
                self.send_response(200)
                self.send_header("Content-type", "application/json")
                self.end_headers()
        self.wfile.write(json.dumps(response).encode('utf-8'))
        return

def main():   
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        pass

    webServer.server_close()
    print("Server stopped.")


if __name__ == "__main__":
    main()