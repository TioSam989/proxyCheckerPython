import re


def validate_proxy(proxy_string):
    pattern = r"^(?:(http|https|socks4|socks5):\/\/)?\d{1,3}(\.\d{1,3}){3}:\d{1,5}$"
    return bool(re.match(pattern, proxy_string, re.IGNORECASE))


def format_proxy_to_object(proxy_string, req_type=None):
    if "://" in proxy_string:
        protocol, address_port = proxy_string.split("://")
    else:
        protocol = req_type if req_type else "http"
        address_port = proxy_string

    address, port = address_port.split(":")

    return (protocol, address, port)


def filter_active_proxies(proxy_list, fn_test, fn_format, tqdm_pkg):
    active_proxies = []

    for proxy in tqdm_pkg(proxy_list, desc="Testing Proxies", unit="proxy"):
        proxy_conf = fn_format(proxy)
        is_active, _, _ = fn_test(*proxy_conf)
        if is_active:
            active_proxies.append(proxy)

    return active_proxies
