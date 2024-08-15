import requests


def handle_list_url(domain, file_url):
    response = requests.get(file_url)
    if response.status_code == 200:
        new_list = []
        # Split the content by lines and process each line
        for line in response.text.splitlines():
            # Split the line at the first space and keep only the part before it
            proxy = line.split(" ")[0]
            full_url = f"{domain}://{proxy}"
            new_list.append(full_url)
        return new_list
    else:
        print("Failed to retrieve the file.")
        return []
