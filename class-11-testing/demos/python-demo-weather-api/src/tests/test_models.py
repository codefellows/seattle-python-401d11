from src.models import City


class TestClass:
    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup_method(self, method):
        pass

    def teardown_method(self, method):
        pass

    def test_create_city(self, session):
        city = City(name='Bellevue', zipcode='98038')

        session.add(city)
        session.commit()

        assert city.id > 0

        cities = City.query.all()

        assert len(cities) == 1

        assert cities[0].name == 'Bellevue'

    def test_create_city_again(self, session):
        city = City(name='Bellevue', zipcode='98038')
        session.add(city)
        session.commit()

        assert city.id > 0

        cities = City.query.all()

        assert len(cities) == 1

    def test_tc2(self):
        pass
