#!/bin/bash

# ----------------------------------------------
# Streamlit Port Scanner - Installation & Usage
# ----------------------------------------------

# This script will guide you through the installation and usage of the Streamlit Port Scanner app.

echo "----------------------------------------------"
echo "Streamlit Port Scanner"
echo "A simple and lightweight port scanner web application built using Python and Streamlit."
echo "It allows users to input a target IP address and scan a range of ports to determine which are open or closed."
echo "----------------------------------------------"

echo ""
echo "Features:"
echo "- Input target IP address and custom port range"
echo "- Scan ports directly from a web browser"
echo "- Display real-time results with port status"
echo "- Easy to set up and run locally"
echo ""

# STEP 1: Clone the repository
echo "1. Clone the Repository"
echo "------------------------------------"
git clone https://github.com/<your-username>/streamlit-port-scanner.git
cd streamlit-port-scanner

# STEP 2: Create and Activate a Virtual Environment (Optional)
echo "2. (Optional) Create and Activate a Virtual Environment"
echo "------------------------------------"
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# STEP 3: Install Required Dependencies
echo "3. Install Required Dependencies"
echo "------------------------------------"
pip install streamlit

# STEP 4: Create Python application file
echo "4. Creating the Python application file (port_scanner.py)..."
cat <<EOF > port_scanner.py
import socket
import streamlit as st

def scan_port(ip, port):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result = s.connect_ex((ip, port))
        if result == 0:
            return f"Port {port}: OPEN"
        else:
            return f"Port {port}: CLOSED"
        s.close()
    except socket.error:
        return f"Port {port}: ERROR"

def main():
    st.title("Port Scanner")
    ip = st.text_input("Target IP Address:")
    start_port = st.number_input("Start Port", min_value=1, max_value=65535, value=1)
    end_port = st.number_input("End Port", min_value=1, max_value=65535, value=1024)

    if st.button("Start Scan"):
        if ip and start_port and end_port:
            st.write(f"Scanning ports {start_port} to {end_port} on {ip}...")
            results = []
            for port in range(start_port, end_port + 1):
                result = scan_port(ip, port)
                results.append(result)
            for result in results:
                st.write(result)
        else:
            st.error("Please enter a valid IP address and port range.")

if __name__ == "__main__":
    main()
EOF

# STEP 5: Run the Application
echo "5. Run the Application"
echo "------------------------------------"
streamlit run port_scanner.py

# ----------------------------------------------
echo "Access the web app in your browser at: http://localhost:8501"
echo "----------------------------------------------"

# NOTES
echo "Notes:"
echo "- This scanner uses sequential scanning, so scanning a large range may take time."
echo "- For performance improvements, consider adding multithreading or asyncio."
echo "- Use this tool ethically — only scan IP addresses you own or have permission to test."
echo "- The app uses the socket library and connects via TCP."
echo ""

# License Information
echo "License: This project is licensed under the MIT License."
echo ""

# END OF SCRIPT
