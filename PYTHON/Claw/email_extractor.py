import re
import requests

def extract_email_addresses(url):
    response = requests.get(url)
    if response.status_code == 200:
        page_content = response.text
        email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        email_addresses = re.findall(email_pattern, page_content)
        return email_addresses
    else:
        print(f"Failed to retrieve page content from {url}")
        return []

# Example usage
search_query = 'Realtor'  # Replace with your desired search query
num_pages = 2  # Number of search result pages to scrape

output_file = "email_addresses.txt"  # Path to the output file

with open(output_file, "w") as file:
    for page in range(num_pages):
        start_index = page * 10
        search_url = f"https://www.google.com/search?q={search_query}&start={start_index}"
        search_results = requests.get(search_url)
        if search_results.status_code == 200:
            search_results_content = search_results.text
            search_result_urls = re.findall(r'<a href="/url\?q=(.*?)"', search_results_content)
            for url in search_result_urls:
                email_addresses = extract_email_addresses(url)
                if email_addresses:
                    file.write(f"Email addresses found on {url}:\n")
                    for email in email_addresses:
                        file.write(email + "\n")
                else:
                    file.write(f"No email addresses found on {url}\n")
        else:
            print(f"Failed to retrieve search results for {search_query}")

print(f"Email addresses extracted and saved to {output_file}")
