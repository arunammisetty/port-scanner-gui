# Network Port Scanner GUI

A simple and lightweight **port scanner web application** built using **Python** and **Streamlit**. It allows users to input a target IP address and scan a range of ports to determine which are open or closed.

## Features

- Input target IP address and custom port range
- Scan ports directly from a web browser
- Display real-time results with port status
- Easy to set up and run locally

---

## Installation

Follow the steps below to install and run the app:

### 1. Clone the Repository

```bash
git clone https://github.com/<your-username>/streamlit-port-scanner.git
cd streamlit-port-scanner

2. (Optional) Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to avoid dependency conflicts.

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

3. Install Required Dependencies

pip install streamlit

4. Run the Application

streamlit run port_scanner.py

5. Access the Web App

Streamlit will automatically open the app in your browser.
If it doesn't, navigate to:

http://localhost:8501


---

Usage

1. Enter the target IP address (e.g., 192.168.1.1 or scanme.nmap.org).


2. Specify the start port and end port for scanning.


3. Click the Start Scan button to begin scanning.


4. View the real-time status of each port in the web interface.




---

Code Overview

Here's the Python code that powers the Streamlit app:

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


---

Notes

This scanner uses sequential scanning, so scanning a large range of ports may take some time.

For performance improvements, consider adding multithreading or asyncio.

Use this tool ethically — only scan IP addresses you own or have permission to test.

The app uses the socket library and connects via TCP.



---

License

This project is licensed under the MIT License.


---

Additional Information

Requirements: Python 3.x, Streamlit

Contributions: Contributions are welcome! Please open an issue or submit a pull request.

Issues: If you encounter any bugs or issues, please report them on the Issues page.


### Explanation:
- The content is fully written in **Markdown** syntax with proper section headers, code blocks, and instructions.
- Code snippets are enclosed with triple backticks (```python) for Python code.
