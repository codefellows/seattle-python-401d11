from ..models import User

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
        assert User.check_password_hash(user, 'secret')

    def test_password_check(self, user):
        assert User.check_password_hash(user, 'secret')