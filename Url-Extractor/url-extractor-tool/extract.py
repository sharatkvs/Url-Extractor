import requests
import re

def extract_urls(target_url):
    try:
        # Fetch the webpage content
        response = requests.get(target_url)
        response.raise_for_status()  # Check for HTTP request errors

        # Extract URLs using regex
        urls = re.findall(r'href=["\'](https?://.*?)[\'"]', response.text)
        return urls
    except requests.exceptions.RequestException as e:
        print(f"Error fetching the URL: {e}")
        return []

# Input from user
url = input("Enter the website URL: ")
extracted_urls = extract_urls(url)

# Display results
if extracted_urls:
    print("\nExtracted URLs:")
    for link in extracted_urls:
        print(link)
else:
    print("No URLs found.")
