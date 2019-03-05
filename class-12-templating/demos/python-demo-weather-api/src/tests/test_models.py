from src.models import City


class TestModels:
    def test_create_city(self, city):
        assert city.id > 0

    def test_city_name(self, city):
        assert city.name == 'Bellevue'

    def test_city_zip(self, city):
        assert city.zipcode == '98038'
