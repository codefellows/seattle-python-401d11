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

    def test_city_category_id(self, city):
        """
        """
        assert city.category_id > 0


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

    def test_category_user_id(self, category):
        """
        """
        assert category.user_id > 0


class TestUserModel:
    """
    """
    def test_user_create(self, user):
        """
        """
        assert user.id > 0

    def test_user_email(self, user):
        """
        """
        assert user.email == 'default@example.com'

    def test_user_check_password(self, user):
        """
        """
        from src.models import User
        assert User.check_password_hash(user, 'secret')
