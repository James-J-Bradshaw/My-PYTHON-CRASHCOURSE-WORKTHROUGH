from testing_code_exercises import city_country

def test_city_country():
        """Do cities and countries like London, 
        Britain work in this function"""
        city_and_country = city_country("London", "Britain")
        assert city_and_country == "London, Britain"

def test_city_country_and_population():
        """If I include a population count, will the function still work"""
        city_and_country = city_country("London", "Britain", 50)
        assert city_and_country == "London, Britain - Population 50"