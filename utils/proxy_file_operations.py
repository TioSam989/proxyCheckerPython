def read_proxies_from_file(file_path, validate_proxy_func):
    proxies = []
    with open(file_path, "r") as file:
        for line in file:
            line = line.strip()
            if not line or line.startswith("#"):
                continue 
            if validate_proxy_func(
                line
            ): 
                protocol, rest = line.split("://")
                url, port = rest.split(":")
                proxies.append((protocol, url, port))  
    return proxies


def save_successful_proxies(proxies, file_path):
    try:
        with open(file_path, "w") as file:
            for proxy_type, url, port in proxies:
                file.write(f"{proxy_type}://{url}:{port}\n")
        print("Saved successfully!")
    except Exception as e:
        print(f"Failed to save successful proxies: {e}")


def add_proxies_to_file(new_proxy, file_path):
    try:
        with open(file_path, "a+") as file_object:

            file_object.seek(0)

            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(new_proxy)
        print("Added successfully!")
    except Exception as err:
        print(f"Failed to add proxie: {err}")
