import requests
from bs4 import BeautifulSoup

def scrape_roofing_companies(city):
    url = "https://www.homeadvisor.com/c-{}-Roofing.html".format(city)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    company_data = []
    companies = soup.find_all("div", class_="company-info")

    for company in companies:
        name = company.find("h3").text.strip()
        address = company.find("div", class_="address").text.strip()
        email = company.find("a", class_="email").text.strip()
        phone = company.find("span", class_="phone").text.strip()
        home_address = company.find("div", class_="home-address").text.strip()

        company_data.append([name, address, email, phone, home_address])

    return company_data

def generate_html_table(data):
    html = "<table>\n"
    html += "<tr><th>Company Name</th><th>Address</th><th>Email Address</th><th>Phone Number</th><th>Home Address</th></tr>\n"

    for row in data:
        html += "<tr>"
        for item in row:
            html += f"<td>{item}</td>"
        html += "</tr>\n"

    html += "</table>"
    return html

# Specify the list of cities for scraping roofing companies
cities = ["New-York-NY", "Los-Angeles-CA", "Chicago-IL"]

# Scrape roofing company information for each city
all_roofing_data = []
for city in cities:
    roofing_data = scrape_roofing_companies(city)
    all_roofing_data.extend(roofing_data)

# Generate HTML table
html_table = generate_html_table(all_roofing_data)

# Save the HTML table to a file
with open("roofing_companies.html", "w") as file:
    file.write(html_table)

