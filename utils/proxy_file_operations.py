def read_proxies_from_file(file_path):
    proxies = []
    with open(file_path, "r") as file:
        for line in file:

            line = line.strip()

            if not line:
                continue

            proxy_part, comment_part = (
                line.split("#", 1) if "#" in line else (line, None)
            )

            proxy_type, _, rest = proxy_part.partition("://")
            ip_port = rest.split(":")
            ip = ip_port[0]
            port = int(ip_port[1])

            proxies.append((proxy_type, ip, port))

    return proxies


def save_successful_proxies(proxies, filename):
    try:
        with open(filename, "w") as file:
            for proxy_type, url, port in proxies:
                file.write(f"{proxy_type}://{url}:{port}\n")
        print("Saved successfully!")
    except Exception as e:
        print(f"Failed to save successful proxies: {e}")
