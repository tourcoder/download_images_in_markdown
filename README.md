# Download images in markdown files

This script searches for all markdown files in a specified directory, extracts image URLs that start with
"https://storage.tourcoder.com/", and downloads these images to the destination folder.

Tips: You can set your own Regular expression rules.

### Requirements:
- Python 3
- requests library (install via `pip install requests`)

### Usage:
- Save this script as `download_images_in_markdown.py`.
- Run the script using `python3 download_images_in_markdown.py`.
- Enter the directory path to search for markdown files when prompted (Absolute Path).
- Enter the destination folder to save all images (Absolute Path).

### Functions:
- find_markdown_files(directory): Finds all markdown files in the specified directory.
- extract_image_urls(markdown_content): Extracts all image URLs that start with "https://storage.tourcoder.com/" from the markdown content.
- download_image(url, dest_folder): Downloads an image from the specified URL to the destination folder.
- main(directory, dest_folder): Main function to orchestrate the searching, extracting, and downloading process.

### License
MIT