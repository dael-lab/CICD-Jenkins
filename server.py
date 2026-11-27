from http.server import BaseHTTPRequestHandler, HTTPServer
from contextlib import redirect_stdout
from app import main
import io

class RequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        output = io.StringIO()

        with redirect_stdout(output):
            main()


        response = output.getvalue().encode("utf-8")

        self.send_response(200)
        self.send_header("Content-Type", "text/plain; charset=utf-8")
        self.send_header("Content-Length", str(len(response)))
        self.end_headers()
        self.wfile.write(response)


if __name__ == "__main__":
    server = HTTPServer(("0.0.0.0", 8000), RequestHandler)
    print("Server running on port 8000")
    server.serve_forever()
