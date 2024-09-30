
# Proxy Manager
![Logo](https://raw.githubusercontent.com/TioSam989/proxyCheckerPython/refs/heads/main/print.png)


## Overview
Proxy Manager is a Python-based tool for managing and testing HTTP, HTTPS, SOCKS4, and SOCKS5 proxies. It allows you to import proxies from URLs (e.g., GitHub-hosted text files), test their validity, and save or copy successful ones.

## Features
- **Validate Proxies**: Checks if a proxy follows the correct format.
- **Test Proxies**: Tests the connectivity of HTTP/HTTPS/SOCKS proxies.
- **Import Proxies**: Import proxies from a `.txt` file hosted on GitHub.
- **Filter Proxies**: Test and filter working proxies from a list.
- **Save and Copy Proxies**: Save working proxies to a file or copy them to your clipboard.

## Requirements
- Python 3.x
- `requests`
- `pyperclip`
- `simple_term_menu`
- `tqdm`
- `ProxyChecker` (for testing proxies)


## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/proxy-manager.git
   cd proxy-manager
2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt

## Usage
1. Run the main application with:
   ```bash
   python3 app.py

## Authors

- [@TioSam989](https://www.github.com/TioSam989)


## License

[MIT](https://github.com/TioSam989/proxyCheckerPython/blob/main/LICENSE)

