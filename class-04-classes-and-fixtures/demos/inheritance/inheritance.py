"""
Object Oriented Programming examples.
Classes and Inheritance
Public vs Private vs Protected
@classmethod, @staticmethod decorators
"""


class Human:
    height = 0

    def get_height(self):
        """"""
        raise NotImplementedError


class Person(Human):
    """
    document already
    """

    # protected vs private
    __inner_thoughts = ['sadness','happiness']

    def __init__(self, first_name, age, *children):
        self.first_name = first_name
        self.years_old = age
        self.children = children

        # if not self.children:
        #     self.children = []

        for child in self.children:
            # do something with child
            print(child)

    def die(self):
        print('dead')



    def get_height(self):
        """Uncomment this when switching tests for demonstrating the NotImplementedError
        """
        return f'{self.first_name} is {self.height} inches tall.'


class Employee(Person):
    def __init__(self, emp_id, name, age, children=None):
        if type(emp_id) is not int:
            raise TypeError('Employee ID must be valid integer')

        self.emp_id = emp_id
        # self.emp_id = emp_id if type(emp_id) is int else None
        super().__init__(name, age, children)

    def __repr__(self):
        return f'<Employee ID: {self.emp_id}, Name: {self.first_name}>'

    def __str__(self):
        return f'Name: {self.first_name}, ID: {self.emp_id}'

    def _private_method(self):
        pass

    def say_name(self):
        return f'Hello my name is {self.first_name}'

    @classmethod # @staticmethod
    def hire_new_employee(cls):
        #
        pass

if __name__ == "__main__":
    dan = Employee(123, 'dan',89)
    print(dan)

    def print_pair(a, b):
        print(a, b)
        
    def add_children(*args):
        print_pair(*args)


    add_children('Jane','John')

    Employee.hire_new_employee()
    