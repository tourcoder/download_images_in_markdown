"""
This script searches for all markdown files in a specified directory, extracts image URLs that start with
"https://storage.tourcoder.com/", and downloads these images to the destination folder.

Tips: You can set your own Regular expression rules.

Requirements:
- Python 3
- requests library (install via `pip install requests`)

Usage:
- Save this script as download_images_in_markdown.py.
- Run the script using `python3 download_images_in_markdown.py`.
- Enter the directory path to search for markdown files when prompted (Absolute Path).
- Enter the destination folder to save all images (Absolute Path).

Functions:
- find_markdown_files(directory): Finds all markdown files in the specified directory.
- extract_image_urls(markdown_content): Extracts all image URLs that start with "https://storage.tourcoder.com/" from the markdown content. You can use your
- download_image(url, dest_folder): Downloads an image from the specified URL to the destination folder.
- main(directory, dest_folder): Main function to orchestrate the searching, extracting, and downloading process.

Author: Bin Hua <code@tourcoder.com>
Date: 07-10-2024
"""
import os
import re
import requests

def find_markdown_files(directory):
    """Find all markdown files in the specified directory."""
    markdown_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def extract_image_urls(markdown_content):
    """Extract all image URLs from markdown content that start with https://storage.tourcoder.com/."""
    img_regex = re.compile(r'!\[.*?\]\((https://storage\.tourcoder\.com/.*?)\)')
    return img_regex.findall(markdown_content)

def download_image(url, dest_folder):
    """Download an image from the specified URL to the destination folder."""
    if not os.path.exists(dest_folder):
        os.makedirs(dest_folder)
    try:
        response = requests.get(url)
        response.raise_for_status()
        filename = os.path.join(dest_folder, os.path.basename(url))
        with open(filename, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded {url} to {filename}")
    except Exception as e:
        print(f"Failed to download {url}: {e}")

def main(directory, dest_folder):
    print(f"Searching for markdown files in: {directory}")
    markdown_files = find_markdown_files(directory)
    print(f"Found {len(markdown_files)} markdown files.")
    for markdown_file in markdown_files:
        print(f"Processing file: {markdown_file}")
        with open(markdown_file, 'r', encoding='utf-8') as f:
            content = f.read()
        image_urls = extract_image_urls(content)
        print(f"Found {len(image_urls)} image URLs in {markdown_file}.")
        for url in image_urls:
            print(f"Downloading image: {url}")
            download_image(url, dest_folder)

if __name__ == "__main__":
    source_directory = input("Enter the directory to search for markdown files: ")
    destination_folder = input("Enter the directory to save downloaded images: ")
    main(source_directory, destination_folder)