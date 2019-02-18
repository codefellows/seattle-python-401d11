# Getting Python and pip

## What is Python?

[General Python FAQ](https://docs.python.org/3/faq/general.html){:target="_blank"}

Python is a clear and powerful object-oriented programming language, comparable to Perl, Ruby, Scheme, or Java.

Some of Python's notable features:

- Uses an elegant syntax, making the programs you write easier to read.
- Is an easy-to-use language that makes it simple to get your program working. This makes Python ideal for prototype development and other ad-hoc programming tasks, without compromising maintainability.
- Comes with a large standard library that supports many common programming tasks such as connecting to web servers, searching text with regular expressions, reading and modifying files.
- Python's interactive mode makes it easy to test short snippets of code. There's also a bundled development environment called IDLE.
- Is easily extended by adding new modules implemented in a compiled language such as C or C++.
- Can also be embedded into an application to provide a programmable interface.
- Runs anywhere, including Mac OS X, Windows, Linux, and Unix, with unofficial builds also available for Android and iOS.

Is free software in two senses. It doesn't cost anything to download or use Python, or to include it in your application. Python can also be freely modified and re-distributed, because while the language is copyrighted it's available under an open source license.

Some programming-language features of Python are:

- A variety of basic data types are available: numbers (floating point, complex, and unlimited-length long integers), strings (both ASCII and Unicode), lists, and dictionaries.
- Python supports object-oriented programming with classes and multiple inheritance.
- Code can be grouped into modules and packages.
- The language supports raising and catching exceptions, resulting in cleaner error handling.
- Data types are strongly and dynamically typed. Mixing incompatible types (e.g. attempting to add a string and a number) causes an exception to be raised, so errors are caught sooner.
- Python contains advanced programming features such as generators and list comprehensions.
- Python's automatic memory management frees you from having to manually allocate and free memory in your code.

#### What's new in Python 3:
[Review here](https://docs.python.org/3/whatsnew/3.0.html){:target="_blank"}

## Installing Python

**On Mac:**
- `brew install python3`
Homebrew will take care of the installations for you, and will also lend itself to supporting other installations that we'll make along the way.

**On Linux (Ubuntu) and Windows:**
- [Python Downloads and Instructions for Installation](https://www.python.org/downloads/){:target="_blank"}

## Installing PipEnv

**On Mac:**
- `brew install pipenv`
Again, Homebrew will take care of the installation for you, and simplify things later on.

**On Linux (Ubuntu) and Windows:**
Just use pip:
```sh
$ pip install pipenv
```
Or, if you’re using Ubuntu 17.10:
```sh
$ sudo apt install software-properties-common python-software-properties
$ sudo add-apt-repository ppa:pypa/ppa
$ sudo apt update
$ sudo apt install pipenv
```
