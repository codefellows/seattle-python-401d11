from django.test import TestCase
from ..kanban_project.factories import UserFactory, CategoryFactory, CardFactory


class TestCategoryModels(TestCase):
    def setUp(self):
        self.category = CategoryFactory(
            name='test name',
            description='test desc'
        )

    def test_default_category_attrs(self):
        self.assertEqual(self.category.name, 'test name')
        self.assertEqual(self.category.description, 'test desc')


class TestCardModels(TestCase):
    pass
