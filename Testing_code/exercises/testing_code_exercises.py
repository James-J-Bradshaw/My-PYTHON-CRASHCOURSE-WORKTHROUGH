def city_country(city, country, population=""):
    if population:
        city_and_country = f"{city}, {country} - Population {population}"
    else:
        city_and_country = f"{city}, {country}"
    return city_and_country.title()