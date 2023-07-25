from bs4 import BeautifulSoup
import requests
import re

#Define a function to search for keywords:
def find_book_keywords(book_title):
    keywords = []
    base_url = "https://www.amazon.com/s?k="
    search_url = base_url + book_title.replace(" ", "+")

    response = requests.get(search_url)
    soup = BeautifulSoup(response.content, "html.parser")

    # Find all the search result links
    search_results = soup.find_all("a", class_="a-link-normal a-text-normal")
    for result in search_results:
        link = result.get("href")
        if link.startswith("/s?"):
            # Extract the ASIN from the search result URL
            asin = re.search(r"/dp/(\w+)/", link)
            if asin:
                asin = asin.group(1)
                # Construct the URL for the book's product page
                product_url = f"https://www.amazon.com/dp/{asin}"
                product_response = requests.get(product_url)
                product_soup = BeautifulSoup(product_response.content, "html.parser")

                # Extract keywords from the product description, title, or other relevant sections
                # Customize this part based on the desired location to extract keywords
                product_keywords = product_soup.find("div", class_="productDescriptionWrapper").text
                keywords.extend(product_keywords.lower().split())

    return keywords

#Call the functions and retrieve the keywords:
book_title = "Your Book Title"
keywords = find_book_keywords(book_title)
print(keywords)

