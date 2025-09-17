import socket

def scan_port(host, port):
    """
    Scans a single port on a given host.
    """
    try:
        # Create a new socket object
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        # Set a timeout for the connection attempt
        s.settimeout(1)
        
        # Attempt to connect to the host and port
        result = s.connect_ex((host, port))
        
        # If the connection result is 0, the port is open
        if result == 0:
            print(f"Port {port} is OPEN")
        else:
            print(f"Port {port} is CLOSED or FILTERED")
            
        # Close the socket
        s.close()
        
    except socket.gaierror:
        print("Hostname could not be resolved. Please check the hostname or IP address.")
    except socket.error:
        print("Could not connect to server.")

if __name__ == "__main__":
    # Example usage:
    target_host = input("Enter the host to scan (e.g., example.com or 127.0.0.1): ")
    target_port = int(input("Enter the port number to scan (e.g., 80 or 443): "))
    
    scan_port(target_host, target_port)