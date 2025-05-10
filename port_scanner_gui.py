import socket
import threading
import streamlit as st

# Function to scan a single port
def scan_port(ip, port):
    try:
        # Create a socket and try to connect to the target IP and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Set timeout to 1 second
        result = s.connect_ex((ip, port))  # Connect to the port
        if result == 0:
            return f"Port {port}: OPEN"
        else:
            return f"Port {port}: CLOSED"
        s.close()
    except socket.error:
        return f"Port {port}: ERROR"

# Main Streamlit UI
def main():
    st.title("Port Scanner")

    # User inputs
    ip = st.text_input("Target IP Address:")
    start_port = st.number_input("Start Port", min_value=1, max_value=65535, value=1)
    end_port = st.number_input("End Port", min_value=1, max_value=65535, value=1024)

    # Start scan button
    if st.button("Start Scan"):
        if ip and start_port and end_port:
            st.write(f"Scanning ports {start_port} to {end_port} on {ip}...")
            
            # Scan the range of ports and display results
            results = []
            for port in range(start_port, end_port + 1):
                result = scan_port(ip, port)
                results.append(result)

            # Show the results
            for result in results:
                st.write(result)
        else:
            st.error("Please enter a valid IP address and port range.")

# Run the app
if __name__ == "__main__":
    main()
