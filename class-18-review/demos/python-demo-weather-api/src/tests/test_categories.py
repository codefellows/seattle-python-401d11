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

