import http.server
import socketserver

# Set the port you want the server to run on (e.g., 8080)
PORT = 8080

# Create a request handler to serve files
Handler = http.server.SimpleHTTPRequestHandler

# Create a socket server that listens on the specified port
with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving at port {PORT}")
    
    # Start the server and keep it running until manually terminated
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nServer stopped by user.")
