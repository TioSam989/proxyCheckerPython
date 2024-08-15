import re


def validate_proxy(proxy_string):
    pattern = r"^(http|https|socks4|socks5):\/\/\d{1,3}(\.\d{1,3}){3}:\d{1,5}$"

    if re.match(pattern, proxy_string):
        return True
    else:
        return False
