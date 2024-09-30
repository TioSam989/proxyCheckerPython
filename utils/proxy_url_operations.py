import requests


def handle_list_url(domain, github_file_url):

    if not github_file_url.startswith("https://raw.githubusercontent.com/"):
        print("Only GitHub raw URLs are supported.")
        return []

    try:
        response = requests.get(github_file_url)

        if response.status_code == 200:
            new_list = []

            for line in response.text.splitlines():
                line = line.strip()

                if line:
                    proxy = line.split(" ")[0]
                    full_url = f"{domain}://{proxy}"
                    new_list.append(full_url)

            return new_list

        else:
            print(f"Failed to retrieve the file. HTTP Status: {response.status_code}")
            return []

    except requests.exceptions.RequestException as e:
        print(f"An error occurred while fetching the file: {e}")
        return []
