# app.py
import sys
from utils.proxy_tester import test_http_https_proxy

def main():

    proxy_list = [
        ("http", "202.137.144.228", 8080),
        ("http", "162.55.26.132", 31280),
        ("http", "52.191.208.232", 80),
        ("socks4", "162.240.239.103", 31854),
        ("socks4", "50.218.57.71", 80),
        ("socks4", "65.49.82.7", 48859),
    ]

    for proxy_type, url, port in proxy_list:
        success, message = test_http_https_proxy(proxy_type, url, port)
        print(message)


if __name__ == "__main__":
    main()
