import requests # type: ignore

# from proxy_validators import validate_proxy

def test_http_https_proxy(type, url, port):
    proxy_url = f"{type}://{url}:{port}"

    try:
        
        # if validate_proxy:
        #     print("Wrong Format")
        #     raise Exception("Wrong Format")
        
        if type.startswith("socks"):
            proxies = {
                "http": proxy_url,
                "https": proxy_url,
            }
        else:
            proxies = {
                type: proxy_url,
                type.replace("http", "https"): proxy_url,
            }

        res = requests.get("https://example.com", proxies=proxies, timeout=10)

        if res.status_code == 200:
            return True, f"{proxy_url} proxy is working."
        else:
            return (
                False,
                f"{proxy_url} proxy failed with status code {res.status_code}.",
            )
    except Exception as err:
        return False, f"{err}"
