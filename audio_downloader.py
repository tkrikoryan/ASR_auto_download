import requests
from bs4 import BeautifulSoup
import os

# The URL of the page with the links to the MP3 files
base_url = 'https://media.talkbank.org/childes/Eng-UK/Edinburgh/' # can be changed 

# Folder where you want to save the MP3 files
save_folder = 'C:\\Users\\where\\you\\want\\to\\save'

# Make sure the save directory exists
os.makedirs(save_folder, exist_ok=True)

# Send a GET request to the URL
response = requests.get(base_url)

# Parse the content of the page with BeautifulSoup
soup = BeautifulSoup(response.content, 'html.parser')

# Find all the links on the page
links = soup.find_all('a')

# Filter out the links that end with '.mp3'
mp3_links = [link.get('href') for link in links if link.get('href').endswith('.mp3')]

# Download each MP3 file
for mp3_link in mp3_links:
    full_url = base_url + mp3_link
    mp3_response = requests.get(full_url)
    
    if mp3_response.status_code == 200:
        # Construct a valid file name from the link
        file_name = mp3_link.split('/')[-1]
        file_path = os.path.join(save_folder, file_name)
        
        # Write the content to a file
        with open(file_path, 'wb') as file:
            file.write(mp3_response.content)
        print(f"Downloaded {file_name}")
    else:
        print(f"Failed to download {mp3_link}")

print("All downloads complete.")
