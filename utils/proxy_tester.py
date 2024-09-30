from time import sleep
from proxy_checker import ProxyChecker


def test_http_https_proxy(proxy_type, url, port):
    
    proxy_url = f"{proxy_type}://{url}:{port}"
    checker = ProxyChecker()

    try:
        result = checker.check_proxy(proxy_url)

        if result is not None:
            return True, f"{proxy_url} is working.", result
        else:
            return False, f"{proxy_url} failed with result: {result}.", None
    except Exception as err:
        return False, f"Error testing {proxy_url}: {err}", None
