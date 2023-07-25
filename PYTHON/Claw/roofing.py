import requests
import BeautifulSoup

def scrape_roofing_companies(city):
    url = f"https://www.yellowpages.com/search?search_terms=Roofing+Contractors&geo_location_terms=Gustine%2C+CA/{city}"
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

# Specify the city for scraping roofing companies
city = "Gustine CA"

# Scrape roofing company information
roofing_data = scrape_roofing_companies(city)

# Generate HTML table
html_table = generate_html_table(roofing_data)

# Save the HTML table to a file
with open("roofing_companies.html", "w") as file:
    file.write(html_table)

