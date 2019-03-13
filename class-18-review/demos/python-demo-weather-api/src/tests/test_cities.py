from ..models import City


class TestCityModel:
    """
    """

    def test_no_cities(self, session):
        """
        should start out with no cities in test db
        uses 'session' fixture
        """
        cities = City.query.all()

        assert len(cities) == 0

    def test_create_city(self, city):
        """
        should creata a city with a > 0 id
        via the 'city' fixture
        """
        assert city.id > 0

    def test_city_name(self, city):
        """
        should have correct name from
        'city' fixture
        """
        assert city.name == 'Bellevue'

    def test_city_zip(self, city):
        """
        should have correct zipcode 
        from 'city' fixture
        """
        assert city.zipcode == '98038'

    def test_city_category_id(self, city):
        """
        should have a related category
        in 'city' fixture
        """
        assert city.category.name == 'Default'

    def test_repr(self, city):
        """
        should represent nicely
        """
        assert repr(city) == '<City Bellevue-98038>'
