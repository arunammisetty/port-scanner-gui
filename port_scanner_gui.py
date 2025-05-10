import socket
import threading
import tkinter as tk
from tkinter import messagebox


# Function to scan a single port
def scan_port(ip, port, result_listbox):
    try:
        # Create a socket and try to connect to the target IP and port
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)  # Set timeout to 1 second
        result = s.connect_ex((ip, port))  # Connect to the port
        if result == 0:
            result_listbox.insert(tk.END, f"Port {port}: OPEN")
        else:
            result_listbox.insert(tk.END, f"Port {port}: CLOSED")
        s.close()
    except socket.error:
        result_listbox.insert(tk.END, f"Port {port}: ERROR")
        return


# Function to start scanning for multiple ports
def start_scan():
    ip = ip_entry.get()
    start_port = int(start_port_entry.get())
    end_port = int(end_port_entry.get())
    
    # Validate inputs
    if not ip or not start_port or not end_port:
        messagebox.showerror("Input Error", "Please fill in all fields correctly!")
        return
    
    result_listbox.delete(0, tk.END)  # Clear previous results
    
    # Start scanning in separate threads for each port
    for port in range(start_port, end_port + 1):
        threading.Thread(target=scan_port, args=(ip, port, result_listbox)).start()


# Create the main window
root = tk.Tk()
root.title("Port Scanner")
root.geometry("500x400")

# Create and place the labels and entries for user input
tk.Label(root, text="Target IP Address:").pack(pady=5)
ip_entry = tk.Entry(root, width=40)
ip_entry.pack(pady=5)

tk.Label(root, text="Start Port:").pack(pady=5)
start_port_entry = tk.Entry(root, width=40)
start_port_entry.pack(pady=5)

tk.Label(root, text="End Port:").pack(pady=5)
end_port_entry = tk.Entry(root, width=40)
end_port_entry.pack(pady=5)

# Create and place the button to start scanning
scan_button = tk.Button(root, text="Start Scan", width=20, command=start_scan)
scan_button.pack(pady=20)

# Create and place the Listbox to display results
result_listbox = tk.Listbox(root, width=60, height=10)
result_listbox.pack(pady=10)

# Start the GUI loop
root.mainloop()
