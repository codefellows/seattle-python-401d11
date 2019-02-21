from .inheritance import Person, Employee
import pytest


@pytest.fixture
def sam_person():
    return Person('Sam', 23)


@pytest.fixture
def susan_employee():
    return Employee(1234, 'Susan', 34)


def test_can_create_person():
    # This test does not use the above fixtures
    vinnie = Person('Vinnie', 34)
    assert isinstance(vinnie, Person)


# The below tests will use fixtures
# def test_get_height(sam_person):
#     sam_person.height = 72
#     assert sam_person.get_height() == 72


def test_get_height_not_implemented(sam_person):
    sam_person.height = 72
    with pytest.raises(NotImplementedError):
        sam_person.get_height()


def test_employee_has_first_name(susan_employee):
    assert susan_employee.first_name == 'Susan'


def test_employee_has_employee_id(susan_employee):
    assert susan_employee.emp_id == 1234


def test_employee_id_throws_error_with_non_int():
    with pytest.raises(TypeError):
        Employee([1, 2, 3, 4], 'Susan', 32)


