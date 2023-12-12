import os
from urllib.parse import urlparse

# Step 1: Build a set of expected file paths
expected_paths = set()
base_dir = '/home/ubuntu/Downloads/xiaoqing'
text_file_path = '/home/ubuntu/Downloads/xiaoqing/urls.txt'

with open(text_file_path, 'r') as f:
    for line in f:
        url = line.strip()
        parsed_url = urlparse(url)
        path_segments = parsed_url.path.strip('/').split('/')
        
        # Construct the expected directory path and filename
        repo_dir = path_segments[-3]
        arch_dir = path_segments[-2]
        file_name = path_segments[-1]
        expected_path = os.path.join(base_dir, repo_dir, arch_dir, file_name)
        expected_paths.add(expected_path)

# Step 2: Build a set of actual file paths
actual_paths = set()
for root, dirs, files in os.walk(base_dir):
    for file in files:
        actual_path = os.path.join(root, file)
        actual_paths.add(actual_path)

# Step 3: Compare the two sets to find discrepancies
missing_files = expected_paths - actual_paths
extra_files = actual_paths - expected_paths

# Print the results
if missing_files:
    print("Missing files:")
    for file in missing_files:
        print(file)
else:
    print("No missing files.")

if extra_files:
    print("\nExtra files:")
    for file in extra_files:
        print(file)
else:
    print("\nNo extra files.")

