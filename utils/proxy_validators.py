import re


def validate_proxy(proxy_string):
    pattern = r"^(http|https|socks4|socks5):\/\/\d{1,3}(\.\d{1,3}){3}:\d{1,5}$"

    if re.match(pattern, proxy_string):
        return True
    else:
        return False


def format_proxy_to_object(proxy_string):
    protocol_and_address = proxy_string.split("://")[1]

    address, port = protocol_and_address.split(":")

    return (proxy_string.split("://")[0], address, port)


def filter_active_proxies(proxy_list, fn_test, fn_format, tqdm_pkg):
    active_proxies = []
    for proxy in tqdm_pkg(proxy_list, desc="Testing Proxies", unit="proxy"):
        proxy_conf = fn_format(proxy)
        is_active, _ = fn_test(*proxy_conf)
        if is_active:
            active_proxies.append(proxy)
    return active_proxies