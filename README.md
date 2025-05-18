# Network Port Scanner

A simple and lightweight **port scanner web application** built using **Python** and **Streamlit**. It allows users to input a target IP address and scan a range of ports to determine which are open or closed—all through a clean and interactive web interface.

## Features

- Input target IP address and port range (start and end ports)
- Scan ports directly from your web browser
- Display real-time port status (open/closed)
- Easy to set up and run locally
- Built using Streamlit for a responsive UI

## Installation

Follow these steps to install and run the Streamlit app:

### 1. Clone the Repository

```bash
git clone https://github.com/arunammisetty/port-scanner-gui.git
cd port-scanner-gui
```

### 2. (Optional) Create and Activate a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate
```

### 3. Install Required Dependencies

```bash
pip install streamlit
```

### 4. Run the Application

```bash
streamlit run port_scanner_streamlit.py
```

### 5. Open in Browser

Streamlit will automatically open the app in your default browser.
If it doesn’t, open manually:

```bash
http://localhost:8501
```

# Usage

1. Enter the target IP address (e.g., 192.168.1.1 or scanme.nmap.org)


2. Set the start port and end port


3. Click the "Start Scan" button


4. View the status of each port (open/closed) in the web interface



# Code Overview

```bash
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
```

## Notes

- This scanner uses sequential scanning, which can be slow for large port ranges.

- You can optimize it using multithreading or asyncio for better performance.

- Always scan ethically—only scan IPs you own or have permission to test.

- Uses the socket library to perform TCP port scanning.


## License

This project is licensed under the MIT License.


## Additional Information

Requirements: Python 3.x, Streamlit

Contributions: Contributions are welcome! Please open an issue or pull request.

Issues: Report bugs or feature requests on the Issues page


# Author

© Arun Ammisetty

[Linkedin Profile](https://www.linkedin.com/in/arun-ammisetty)
