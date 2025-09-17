# Python Port Scanner

A simple and efficient port scanner written in Python.

### Features
- Scans a target host for open ports.
- Supports scanning a single port or a range of ports.
- Provides a simple and clean command-line interface.

### How to Use

#### Prerequisites
- Python 3.x
- Xcode Command Line Tools (on macOS)

#### Running the Script

1.  Clone this repository or download the `port_scanner.py` file.
    ```bash
    git clone [https://github.com/jayday83/port-scanner.git](https://github.com/jayday83/port-scanner.git)
    ```
2.  Open your terminal and navigate to the project directory.
    ```bash
    cd port-scanner
    ```
3.  Run the script with the following command:
    ```bash
    python3 port_scanner.py
    ```
4.  The script will prompt you to enter a target IP/hostname and a port or a port range to scan.

### Example Output

Here is what the output of a scan might look like:

Enter host to scan: scanme.nmap.org
Enter port range to scan (e.g., 1-100): 20-30

Scanning host: scanme.nmap.org
Port 22: open
Port 25: closed
Port 80: open
Port 443: open

### License

This project is licensed under the MIT License.
