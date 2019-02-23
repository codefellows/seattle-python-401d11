class Person():
"""
    note below attributes can serve
    as either class or instance attributes.
    Weird, kind of, but that's the way it is
    Which one is which depends on how they were
    accessed
"""
    __population = 0 # mark private
    name = 'unset'

    def __init__(self, name):
        self.name = name
        Person.__population += 1

    def get_name(self):
        return self.name

    @classmethod
    def get_pop(cls):
        return cls.__population

    @staticmethod
    def get_pop_static():
        # only way to access __population to violate privacy
        return Person.__population

if __name__ == "__main__":
    p = Person('Jane')
    print('p.name', p.name)
    print('Person.name',Person.name)
    print('Person.get_pop()', Person.get_pop())
    print(Person.get_pop_static())
