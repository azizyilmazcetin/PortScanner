# Port Scanner

This is a simple port scanner application written in Python. The port scanner can scan a range of ports on a target IP address using either TCP or UDP protocols.

## Features

- Scans a range of ports on a target IP address.
- Supports both TCP and UDP protocols.
- Saves scan results to a text file.

## Requirements

- Python 3.x
- `socket` module (standard library)
- `concurrent.futures` module (standard library)

## Usage

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/PortScanner.git
    cd PortScanner
    ```

2. Run the script:
    ```bash
    python port_scanner.py
    ```

3. Enter the target IP address, start port, end port, and protocol (TCP/UDP) when prompted.

4. The scan results will be saved to `scan_results.txt`.

## Example

```bash
$ python port_scanner.py
Enter target IP address: 192.168.1.1
Enter start port: 1
Enter end port: 1024
Enter protocol (TCP/UDP): TCP

Scan results for 192.168.1.1 from port 1 to 1024 using TCP:

TCP Port 22 is open
TCP Port 80 is open
TCP Port 443 is open
