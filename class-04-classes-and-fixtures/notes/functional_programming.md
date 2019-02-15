# Anonymous Functions and Functional Programming

## Functional Programming [1](https://docs.python.org/3/howto/functional.html#introduction){:target="_blank"}
Programming languages support decomposing problems in several different ways:

- Most programming languages are procedural: programs are lists of instructions that tell the computer what to do with the program’s input. C, Pascal, and even Unix shells are procedural languages.
- In declarative languages, you write a specification that describes the problem to be solved, and the language implementation figures out how to perform the computation efficiently. SQL is the declarative language you’re most likely to be familiar with; a SQL query describes the data set you want to retrieve, and the SQL engine decides whether to scan tables or use indexes, which subclauses should be performed first, etc.
- Object-oriented programs manipulate collections of objects. Objects have internal state and support methods that query or modify this internal state in some way. Smalltalk and Java are object-oriented languages. C++ and Python are languages that support object-oriented programming, but don’t force the use of object-oriented features.
- Functional programming decomposes a problem into a set of functions. Ideally, functions only take inputs and produce outputs, and don’t have any internal state that affects the output produced for a given input. Well-known functional languages include the ML family (Standard ML, OCaml, and other variants) and Haskell.
- The designers of some computer languages choose to emphasize one particular approach to programming. This often makes it difficult to write programs that use a different approach. Other languages are multi-paradigm languages that support several different approaches. Lisp, C++, and Python are multi-paradigm; you can write programs or libraries that are largely procedural, object-oriented, or functional in all of these languages. In a large program, different sections might be written using different approaches; the GUI might be object-oriented while the processing logic is procedural or functional, for example.

In a functional program, input flows through a set of functions. Each function operates on its input and produces some output. Functional style discourages functions with side effects that modify internal state or make other changes that aren’t visible in the function’s return value. Functions that have no side effects at all are called purely functional. Avoiding side effects means not using data structures that get updated as a program runs; every function’s output must only depend on its input.

Some languages are very strict about purity and don’t even have assignment statements such as `a=3` or `c = a + b`, but it’s difficult to avoid all side effects. Printing to the screen or writing to a disk file are side effects, for example. For example, in Python a call to the `print()` or `time.sleep()` function both return no useful value; they’re only called for their side effects of sending some text to the screen or pausing execution for a second.

Python programs written in functional style usually won’t go to the extreme of avoiding all I/O or all assignments; instead, they’ll provide a functional-appearing interface but will use non-functional features internally. For example, the implementation of a function will still use assignments to local variables, but won’t modify global variables or have other side effects.

Functional programming can be considered the opposite of object-oriented programming. Objects are little capsules containing some internal state along with a collection of method calls that let you modify this state, and programs consist of making the right set of state changes. Functional programming wants to avoid state changes as much as possible and works with data flowing between functions. In Python you might combine the two approaches by writing functions that take and return instances representing objects in your application (e-mail messages, transactions, etc.).

Functional design may seem like an odd constraint to work under. Why should you avoid objects and side effects? There are theoretical and practical advantages to the functional style:

- Formal provability.
- Modularity.
- Composability.
- Ease of debugging and testing.


### Iterators [2](https://docs.python.org/3/howto/functional.html#iterators){:target="_blank"}
An iterator is an object representing a stream of data; this object returns the data one element at a time. A Python iterator must support a method called __next__() that takes no arguments and always returns the next element of the stream. If there are no more elements in the stream, __next__() must raise the StopIteration exception. Iterators don’t have to be finite, though; it’s perfectly reasonable to write an iterator that produces an infinite stream of data.

The built-in iter() function takes an arbitrary object and tries to return an iterator that will return the object’s contents or elements, raising TypeError if the object doesn’t support iteration. Several of Python’s built-in data types support iteration, the most common being lists and dictionaries. An object is called iterable if you can get an iterator for it.

You can experiment with the iteration interface manually:
```python
L = [1,2,3]
it = iter(L)
it
# <...iterator object at ...>
it.__next__()  # same as next(it)
# 1
next(it)
# 2
next(it)
# 3
next(it)
# Traceback (most recent call last):
#   File "<stdin>", line 1, in <module>
# StopIteration
```

### Generators [3](https://docs.python.org/3/howto/functional.html#generator-expressions-and-list-comprehensions){:target="_blank"}
List comprehensions and generator expressions (short form: “listcomps” and “genexps”) are a concise notation for such operations, borrowed from the functional programming language Haskell (https://www.haskell.org/). You can strip all the whitespace from a stream of strings with the following code:

```python
line_list = ['  line 1\n', 'line 2  \n']

# Generator expression -- returns iterator
stripped_iter = (line.strip() for line in line_list)
stripped_iter
# <generator object <genexpr> at 0x10aaf1af0>
next(stripped_iter)
# 'line 1'

# List comprehension -- returns list
stripped_list = [line.strip() for line in line_list]
stripped_list
# ['line 1', 'line 2']
```
You can select only certain elements by adding an "if" condition:
```python
stripped_list = [line.strip() for line in line_list if line != ""]
```

## The Lambda Function [4](https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions){:target="_blank"}
Small anonymous functions can be created with the `lambda` keyword. This function returns the sum of its two arguments: `lambda a, b: a+b`. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, `lambda` functions can reference variables from the containing scope:
```python
def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0)
# 42
f(1)
# 43
```
The above example uses a `lambda` expression to return a function. Another use is to pass a small function as an argument:
```python
pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key=lambda pair: pair[1])
pairs
# [(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## Built-in Python Functions
Recall from the description above that functional methods will not mutate the state of the original input. Therefore the following method examples will show the pattern of a mutated copy provided as the return value for each call.

#### sorted()
Returns a new sorted list form the iterable argument
```python
data = [23, 43, 1, 2, 399, 401, 201, 3]
sorted(data)
# [1, 2, 3, 23, 43, 201, 399, 401]  # Return value is a mutated copy
data
# [23, 43, 1, 2, 399, 401, 201, 3]  # Illustrates that the original state is maintained
```

#### map()
Given a function as the first argument and an iterable as the second, the function will be called for each element in the iterable. A new copy of the iterable will be made, and mutations will occur to the copy before finally being returned as an iterator.
```python
squares = [1, 2, 3, 4, 5, 6]

def square(n):
    return n * n

square_data = map(square, squares)
# <map at 0x10aa9ba20>
next(square_data)
# 1
next(square_data)
# 4
next(square_data)
# 9
next(square_data)
# 16
```

#### filter()
Constructs an iterator based on the conditions defined in the first argument, a function. The second argument being the iterable.
```python
data = [23, 43, 1, 2, 399, 401, 201, 3]

def odds(n):
    return n % 2 != 0

odd_nums = filter(odds, data)
next(odd_nums)
# 23

list(odd_nums)
# [43, 1, 399, 401, 201, 3]
```
Two things to note about the final couple lines there... You can pass an iterator into a list constructor to create a list object. Notice that `23` is no longer in the list? When we passed our iterator into `next()` we actually remove that value from the iterator as we process that data... Might be handy later on; just keep that in mind as you work with iterators!
