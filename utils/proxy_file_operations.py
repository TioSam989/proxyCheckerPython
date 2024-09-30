from time import sleep


def read_proxies_from_file(file_path, validate_proxy_func):
    
    proxies = []
    try:
        with open(file_path, "r") as file:
            for line in file:
                line = line.strip()
                if not line or line.startswith("#"):
                    continue  
                if validate_proxy_func(line):
                    try:
                        protocol, address_port = line.split("://")
                        url, port = address_port.split(":")
                        proxies.append((protocol, url, port))
                    except ValueError:
                        print(f"Invalid proxy format: {line}")
        return proxies
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return []


def save_successful_proxies(proxies, file_path):
   
    try:
        with open(file_path, "w") as file:
            for proxy_type, url, port in proxies:
                file.write(f"{proxy_type}://{url}:{port}\n")
        print("Proxies saved successfully!")
    except Exception as e:
        print(f"Failed to save proxies: {e}")


def add_list_proxies_to_file(proxies_list, file_path, format_fn):
    
    try:
        with open(file_path, "a") as file_object:
            for proxy_string in proxies_list:
                try:
                    proxy_type, url, port = format_fn(proxy_string)
                    file_object.write(f"{proxy_type}://{url}:{port}\n")
                except ValueError:
                    print(f"Invalid proxy format: {proxy_string}")
        print("Proxies added successfully!")
        sleep(1)
    except Exception as err:
        print(f"Failed to add proxies: {err}")
        sleep(1)


def add_proxies_to_file(new_proxy, file_path):
    
    try:
        with open(file_path, "a+") as file_object:
            file_object.seek(0)
            data = file_object.read(100)
            if len(data) > 0:
                file_object.write("\n")
            file_object.write(new_proxy)
        print("Proxy added successfully!")
        sleep(1)
    except Exception as err:
        print(f"Failed to add proxy: {err}")
        sleep(1)
