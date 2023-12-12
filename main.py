import os
from urllib.parse import urlparse
import requests
from concurrent.futures import ThreadPoolExecutor

def download_file(url):
    try:
        # Parse the URL to get the segments and filename
        parsed_url = urlparse(url)
        path_segments = parsed_url.path.strip('/').split('/')

        # Ignore the first segment ('pkgs' or the base URL segment)
        # and get the next segments to construct the directory path
        repo_dir = path_segments[-3]
        arch_dir = path_segments[-2]
        file_name = path_segments[-1]

        # Construct the directory path and filename
        dir_path = os.path.join(base_dir, repo_dir, arch_dir)

        # Check if the directories exist, if not create them
        if not os.path.exists(dir_path):
            os.makedirs(dir_path)

        # Download the file and save it in the appropriate directory
        response = requests.get(url)
        with open(os.path.join(dir_path, file_name), 'wb') as file:
            file.write(response.content)

        print(f"Downloaded: {file_name} to {dir_path}")
    except Exception as e:
        print(f"Failed to download {url} due to {e}")


# Specify the base directory where you want to download the files
base_dir = '/home/ubuntu/Downloads/WO538622/'

# Specify the path to your txt file
text_file_path = '/home/ubuntu/Downloads/urls.txt'

# Read the text file line by line
with open(text_file_path, 'r') as f:
    urls = f.readlines()

# Using ThreadPoolExecutor to download files in parallel
try:
    with ThreadPoolExecutor(max_workers=4) as executor:
        executor.map(download_file, [url.strip() for url in urls])
except KeyboardInterrupt:
    print("Script interrupted by user")

# Indicate that the script has finished executing
print("Downloads completed")

