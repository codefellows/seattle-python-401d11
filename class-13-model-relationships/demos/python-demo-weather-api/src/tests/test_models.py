from ..models import City, Category
class TestCityModel:
    """
    """
    def test_create_city(self, city):
        """
        """
        assert city.id > 0

    def test_city_name(self, city):
        """
        """
        assert city.name == 'Bellevue'
        
    def test_city_zip(self, city):
        """
        """
        assert city.zipcode == '98038'

    def test_city_query(self, city):
        """
        """
        cities = City.query.all()
        assert len(cities) == 1



class TestCategoryModel:
    """
    """
    def test_create_category(self, category):
        """
        """
        assert category.id > 0

    def test_category_name(self, category):
        """
        """
        assert category.name is not None


class TestCategoryCityRelationship:
    """
    """
    def test_city_has_category(self):
        rainy = Category(name='rainy')
        seattle = City(name='Seattle', zipcode='98108', category=rainy)

        assert seattle.category.name == 'rainy'

    def test_category_has_cities(self):
        rainy = Category(name='rainy')
        seattle = City(name='Seattle', zipcode='98108', category=rainy)
        glasgow = City(name='Glasgow', zipcode='?????', category=rainy)

        assert rainy.cities[0].name == 'Seattle'
        assert rainy.cities[1].name == 'Glasgow'


