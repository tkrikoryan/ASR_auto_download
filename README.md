# MP3 Batch Downloader

This script is designed to automate the process of downloading all `.mp3` audio files from a specified webpage. It works by scraping the webpage for links ending with `.mp3`, constructing the absolute URLs, and then downloading and saving the files locally.

## Requirements

To run this script, you'll need Python installed on your system, as well as the following Python packages:
- `requests`
- `beautifulsoup4`

You can install these packages using `pip` with the following command:

```bash
pip install requests beautifulsoup4
```

# Usage
To use the script, follow these steps:

- Edit the base_url variable in the script to match the URL of the webpage containing the .mp3 files.
- Edit the save_folder variable to specify the path where you want the downloaded files to be saved.
- Run the script with Python in your terminal or command prompt.

```bash
python mp3_batch_downloader.py
```

# Disclaimer

**Replace the filename `mp3_batch_downloader.py` with whatever you named your script. This README assumes you are using Markdown formatting (common on platforms like GitHub). Make sure to save the README with the `.md` extension, and place it in the same directory as your script for better context and understanding.**
