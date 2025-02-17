import socket

def get_http_headers():
    # Create socket and connect
    mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    mysock.connect(('data.pr4e.org', 80))
    
    # Send HTTP request
    cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()
    mysock.send(cmd)
    
    # Dictionary to store headers
    headers = {}
    
    # Receive and parse headers
    while True:
        data = mysock.recv(512).decode()
        if not data:
            break
            
        # Split headers from body
        header_end = data.find('\r\n\r\n')
        if header_end > 0:
            header_lines = data[:header_end].split('\r\n')
            
            # Parse each header line
            for line in header_lines[1:]:  # Skip first line (HTTP/1.1 200 OK)
                if ':' in line:
                    key, value = line.split(':', 1)
                    headers[key.strip()] = value.strip()
            break
    
    # Close connection
    mysock.close()
    
    # Print required headers
    print("Last-Modified:", headers.get('Last-Modified', 'Not found'))
    print("ETag:", headers.get('ETag', 'Not found'))
    print("Content-Length:", headers.get('Content-Length', 'Not found'))
    print("Cache-Control:", headers.get('Cache-Control', 'Not found'))
    print("Content-Type:", headers.get('Content-Type', 'Not found'))

# Run the function
get_http_headers()