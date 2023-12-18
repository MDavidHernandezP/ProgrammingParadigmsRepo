# Import necessary libraries/modules
import threading
import requests

def download_webpage(url):
    response = requests.get(url)
    content = response.text
    print(f"Downloaded content from {url}")

# List of URLs to download concurrently
urls = ["https://www.upy.edu.mx/en", "https://mail.google.com/mail/u/0/", "https://translate.google.com/"]

# Create threads for each URL
threads = [threading.Thread(target=download_webpage, args=(url,)) for url in urls]

# Start the threads
for thread in threads:
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()
    print("All webpages downloaded successfully.")