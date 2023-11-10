#!../bin/python3

def cities(city, country='USA'):
    """This function tells which country a city is in."""
    info = f'{city.title()} is in {country}'
    print(info)

cities('new york')
cities('alabama')
cities('texas')
cities('rome', 'Italy')