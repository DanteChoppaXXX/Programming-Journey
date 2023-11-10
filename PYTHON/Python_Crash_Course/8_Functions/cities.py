#!../bin/python3

# def cities(city, country='USA'):
#     """This function tells which country a city is in."""
#     info = f'{city.title()} is in {country}'
#     print(info)

# cities('new york')
# cities('alabama')
# cities('texas')
# cities('rome', 'Italy')

def city_country(city, country):
    """Display a city and the country it's in."""
    str_format = f'"{city.title()}, {country.title()}"'
    return str_format

city1 = city_country('new york', 'united states')
city2 = city_country('california', 'united states')
city3 = city_country('new jersey', 'united states')
cities = [city1, city2, city3]
for index, city in enumerate(cities, start=1):
    print(index, city)
