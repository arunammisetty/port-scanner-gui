# Network Port Scanner with GUI

This is a simple port scanner created with **Python** and **Tkinter** for the graphical user interface (GUI). It allows users to scan a range of ports on a target IP address to check whether each port is open or closed.

## Features

- Input a target IP address and port range (start and end ports)
- Start scanning with a button click
- View results in real-time in a listbox
- Simple and easy-to-use GUI

---

## Installation

Follow the steps below to install and run the app:

### 1. Clone the Repository

```bash
git clone https://github.com/arunammisetty/port-scanner-gui.git
cd port-scanner-gui


### 2. (Optional) Create and Activate a Virtual Environment

It is recommended to use a virtual environment to manage dependencies:

python -m venv venv
source venv/bin/activate       # On Windows: venv\Scripts\activate

3. Install Required Dependencies

pip install -r requirements.txt

4. Run the Application

python port_scanner_gui.py


---

Usage

1. Enter the target IP address (e.g., 192.168.1.1 or scanme.nmap.org).


2. Specify the start port and end port for scanning.


3. Click the "Start Scan" button to begin scanning.


4. View the results displayed in the listbox (open or closed ports).




---

Code Overview

Here’s an overview of the Python code for the port scanner:

import socket
import tkinter as tk
from tkinter import messagebox

def scan_port(ip, port):
    try:
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

def start_scan():
    ip = entry_ip.get()
    start_port = int(entry_start_port.get())
    end_port = int(entry_end_port.get())
    results_listbox.delete(0, tk.END)  # Clear previous results

    if ip and start_port and end_port:
        for port in range(start_port, end_port + 1):
            result = scan_port(ip, port)
            results_listbox.insert(tk.END, result)
    else:
        messagebox.showerror("Error", "Please enter valid input.")

# Set up the GUI window
window = tk.Tk()
window.title("Port Scanner")

# Input fields
tk.Label(window, text="Target IP Address:").pack(pady=5)
entry_ip = tk.Entry(window)
entry_ip.pack(pady=5)

tk.Label(window, text="Start Port:").pack(pady=5)
entry_start_port = tk.Entry(window)
entry_start_port.pack(pady=5)

tk.Label(window, text="End Port:").pack(pady=5)
entry_end_port = tk.Entry(window)
entry_end_port.pack(pady=5)

# Scan button
scan_button = tk.Button(window, text="Start Scan", command=start_scan)
scan_button.pack(pady=20)

# Listbox to show the results
results_listbox = tk.Listbox(window, width=50, height=15)
results_listbox.pack(pady=5)

# Run the GUI loop
window.mainloop()


---

Notes

This port scanner uses sequential scanning, so scanning a large range may take time.

For performance improvements, consider adding multithreading or asyncio.

Use this tool ethically — only scan IP addresses you own or have permission to test.

The application uses the socket library for TCP connections.



---

License

This project is licensed under the MIT License.


---

Additional Information

Requirements: Python 3.x, Tkinter

Contributions: Contributions are welcome! Please open an issue or submit a pull request.

Issues: If you encounter any bugs or issues, please report them on the Issues page.



---

Contact

Author: Arun Ammisetty


### Explanation of the Markdown:

- The **README.md** is structured with common sections like Features, Installation, Usage, Code Overview, etc.
- The **Installation** section includes detailed steps to clone the repository, set up the virtual environment, install dependencies, and run the application.
- The **Code Overview** includes the Python code for the **port scanner with GUI**.
- The **Notes** section explains some important details about the tool and performance considerations.
- **License** and **Additional Information** sections include licensing information and contact details.

This should now be ready to be used as the **README.md** file in your GitHub repository.
