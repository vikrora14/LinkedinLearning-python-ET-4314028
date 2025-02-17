import socket

def make_socket_connection():
    try:
        # Create a socket object
        mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Define the host and port
        host = 'data.pr4e.org'  # Example host
        port = 80  # HTTP port
        
        # Connect to the server
        mysock.connect((host, port))
        
        # Create HTTP request
        cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()
        mysock.send(cmd)
        
        # Receive and print data
        while True:
            data = mysock.recv(512)
            if len(data) < 1:
                break
            print(data.decode())
            
        # Close the connection
        mysock.close()
        
    except socket.error as e:
        print(f"Socket error: {e}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    make_socket_connection()