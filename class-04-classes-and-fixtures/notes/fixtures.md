# Pytest Fixtures
The purpose of test fixtures is to provide a fixed baseline upon which tests can reliably and repeatedly execute. `pytest` fixtures offer dramatic improvements over the classic xUnit style of setup/teardown functions:

- Fixtures have explicit names and are activated by declaring their use from test functions, modules, classes or whole projects.
- Fixtures are implemented in a modular manner, as each fixture name triggers a fixture function which can itself use other fixtures.
- Fixture management scales from simple unit to complex functional testing, allowing to parameterize fixtures and tests according to configuration and component options, or to re-use fixtures across function, class, module or whole test session scopes.

In addition, `pytest` continues to support classic xunit-style setup. You can mix both styles, moving incrementally from classic to new style, as you prefer. You can also start out from existing unittest.TestCase style or nose based projects.[1](https://docs.pytest.org/en/latest/fixture.html#pytest-fixtures-explicit-modular-scalable){:target="_blank"}

In short, fixtures allow you to set up dependencies for your test functions to consume, commonly referred to as dependency injection.

## Streamlining Your Tests
Fixtures also allow us the opportunity to maintain DRY code by providing a way to set up and tear down test environments and requirements. If we're aware that we require the same objects or functions for every single test, each of which follows the same setup test over test, why write them multiple times?

Lets create a new fixture!
```python
import pytest

@pytest.fixture  # This is a decorator... more about those later.
def my_fixture():
    # I can do a thing or 10 here to set up my test data
    some_value = 50
    return some_value

def test_a_thing(my_fixture):
    # Passing the fixture in as a parameter to the test allows us to immediately run assertions on that expected return value
    assert my_fixture == 50
```

## Fixture Scope
Fixture Scope defines how often the fixture should execute and how it interacts with your test suite. The options available for defining Scope are:
- `session`: This will run once for the complete pytest session; i.e. all of your test files.
- `module`: This is similar to function scope, but will rather run once for the whole module.
- `class`: This will run once for each test class that the fixture is passed into. We won't use this one for a while.
- `function` _(default)_: This will run once for each tests that the fixture is passed into.

## Parametrized Fixtures
Fixture functions can be parametrized in which case they will be called multiple times, each time executing the set of dependent tests, i. e. the tests that depend on this fixture. Test functions do usually not need to be aware of their re-running. Fixture parametrization helps to write exhaustive functional tests for components which themselves can be configured in multiple ways.[2](https://docs.pytest.org/en/latest/fixture.html#parametrizing-fixtures){:target="_blank"}

## `conftest.py`
If during implementing your tests you realize that you want to use a fixture function from multiple test files you can move it to a `conftest.py` file. You don’t need to import the fixture you want to use in a test, it automatically gets discovered by pytest. The discovery of fixture functions starts at test classes, then test modules, then `conftest.py` files and finally builtin and third party plugins.[3](https://docs.pytest.org/en/latest/fixture.html#conftest-py-sharing-fixture-functions){:target="_blank"}

Using the example from above, we can now separate the fixture from the tests:
```python
# conftest.py
import pytest

@pytest.fixture  # This is a decorator... more about those later.
def my_fixture(scope='module'):
    # I can do a thing or 10 here to set up my test data
    some_value = 50
    return some_value
```
```python
# my_test.py
def test_a_thing(my_fixture):
    # Passing the fixture in as a parameter to the test allows us to immediately run assertions on that expected return value
    assert my_fixture == 50
```

## Fixture Teardown
Pytest supports the execution of fixture specific finalization code when the fixture goes out of scope; i.e. it completes. By using the `yield` keyword rather than `return`, all the code after the `yield` statement serves as the teardown code.
```python
import pytest

@pytest.fixture
def read_file(scope='module'):
    with open('some-file.txt', 'r') as f:
        yield f.read()
    print('teardown file')
    f.close()

# ...some test function which uses the file data
```
