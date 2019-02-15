# Errors in Python

## The Most Common Exceptions
Exceptions are how Python tells you that something has gone wrong. Understanding the standard exception types in Python and what can cause them is very helpful in debugging your code.

There are several exceptions that you are likely to see a lot of:

- NameError: indicates that you have tried to use a symbol that is not bound to a value.
```python
In [13]: does_not_exist
--------------------------------------------------------------------
NameError                          Traceback (most recent call last)
<ipython-input-13-ea972d468210> in <module>()
----> 1 does_not_exist

NameError: name 'does_not_exist' is not defined

In [14]:
```
- TypeError: indicates that you have tried to use the wrong kind of object for an operation.
```python
In [12]: int([1, 2, 3])
--------------------------------------------------------------------
TypeError                          Traceback (most recent call last)
<ipython-input-12-7692ceb95192> in <module>()
----> 1 int([1, 2, 3])

TypeError: int() argument must be a string, a bytes-like object or a number, not 'list'

In [13]:
```
- AttributeError: indicates that you have tried to access an attribute or method that an object does not have (this often means you have a different type of object than you expect).
```python
In [10]: num = 25

In [11]: num.len()
--------------------------------------------------------------------
AttributeError                     Traceback (most recent call last)
<ipython-input-11-f8ba77370ca1> in <module>()
----> 1 num.len()

AttributeError: 'int' object has no attribute 'len'

In [12]:
```
- SyntaxError: indicates that you have mis-typed something.
```python
In [8]: num = 0

In [9]: num 0
File "<ipython-input-9-01735759f7a7>", line 1
    num 0
        ^
SyntaxError: invalid syntax

In [10]:
```
- ValueError: indicates that you provided the right type but an inappropriate value to a built-in function or operation.
```python
In [5]: int('1')
Out[5]: 1

In [6]: int('h')
--------------------------------------------------------------------
ValueError                         Traceback (most recent call last)
<ipython-input-6-9764868dae03> in <module>()
----> 1 int('h')

ValueError: invalid literal for int() with base 10: 'h'

In [7]:
```
- IndexError
```python
In [14]: names = ['zero cool', 'crash overdrive']

In [15]: names[0]
Out[15]: 'zero cool'

In [16]: names[2]
--------------------------------------------------------------------
IndexError                         Traceback (most recent call last)
<ipython-input-16-9f97f8966c5f> in <module>()
----> 1 names[2]

IndexError: list index out of range

In [17]:
```
- KeyError
```python
In [17]: user = {
    ...: 'name': 'slicer',
    ...: 'age': 'unknown',
    ...: }

In [18]: user['wat']
--------------------------------------------------------------------
KeyError                           Traceback (most recent call last)
<ipython-input-18-a702d1aa86c0> in <module>()
----> 1 user['wat']

KeyError: 'wat'
```

_For reference here's an inline list of all the different Error Types that Python provides as built-ins:_  'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'EnvironmentError', 'Exception', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError','NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError',


## Handling Exceptions
_First:_ **Do not raise generic Exceptions. You will have to catch all other more specific exceptions that subclass it.**

It is possible to write programs that handle selected exceptions. Look at the following example, which asks the user for input until a valid integer has been entered, but allows the user to interrupt the program (using Control-C or whatever the operating system supports); note that a user-generated interruption is signalled by raising the `KeyboardInterrupt` exception.
```python
 while True:
     try:
         x = int(input("Please enter a number: "))
         break
     except ValueError:
         print("Oops!  That was no valid number.  Try again...")

```
The try statement works as follows.

- First, the try clause (the statement(s) between the `try` and `except` keywords) is executed.
- If no exception occurs, the except clause is skipped and execution of the `try` statement is finished.
- If an exception occurs during execution of the try clause, the rest of the clause is skipped. Then if its type matches the exception named after the except keyword, the except clause is executed, and then execution continues after the `try` statement.
- If an exception occurs which does not match the exception named in the except clause, it is passed on to outer `try` statements; if no handler is found, it is an unhandled exception and execution stops with a message as shown above.

A `try` statement may have more than one except clause, to specify handlers for different exceptions. At most one handler will be executed. Handlers only handle exceptions that occur in the corresponding try clause, not in other handlers of the same `try` statement. An except clause may name multiple exceptions as a parenthesized tuple, for example:
```python
except (RuntimeError, TypeError, NameError):
    pass
```

## Throwing Exceptions Yourself
One may also instantiate an exception first before raising it and add any attributes to it as desired.
```python
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly,
                         # but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)
# <class 'Exception'>
# ('spam', 'eggs')
# ('spam', 'eggs')
# x = spam
# y = eggs
```
