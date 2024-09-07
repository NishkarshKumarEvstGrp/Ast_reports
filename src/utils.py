
def search_url_in_file(file_path, target_url):
    with open(file_path, 'r') as file:
        for index, url in enumerate(file):
            url = url.strip()
            if url == target_url:
                return index
    return -1

def write_url_to_file(file_path, url):
    with open(file_path, 'a') as file:
        file.write(url + '\n')
    print(f"URL '{url}' appended to file '{file_path}'")



    