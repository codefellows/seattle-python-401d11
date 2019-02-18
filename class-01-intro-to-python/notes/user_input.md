# Command-Line Scripts and User Input

## Running a Python script from the command line

`__main__` is the name of the scope in which top-level code executes. A module’s `__name__` is set equal to `__main__` when read from standard input, a script, or from an interactive prompt.

A module can discover whether or not it is running in the main scope by checking its own `__name__`, which allows a common idiom for conditionally executing code in a module when it is run as a script or with python -m but not when it is imported:

```python
if __name__ == "__main__":
    # execute only if run as a script
    main()
```
For a package, the same effect can be achieved by including a `__main__.py` module, the contents of which will be executed when the module is run with -m.

## Providing Arguments

`python myscript.py [args]`

An interface option terminates the list of options consumed by the interpreter, all consecutive arguments will end up in sys.argv – note that the first element, subscript zero (sys.argv[0]), is a string reflecting the program’s source.

### sys.argv

The list of command line arguments passed to a Python script. `argv[0]` is the script name (it is operating system dependent whether this is a full pathname or not). If the command was executed using the `-c` command line option to the interpreter, `argv[0]` is set to the string `-c`. If no script name was passed to the Python interpreter, `argv[0]` is the empty string.

*Note: To loop over the standard input, or the list of files given on the command line, see the [fileinput](https://docs.python.org/3/library/fileinput.html#module-fileinput){:target="_blank"} module.*

### ArgumentParser

The `argparse` module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and `argparse` will figure out how to parse those out of `sys.argv`. The `argparse` module also automatically generates help and usage messages and issues errors when users give the program invalid arguments.

```python
import argparse

parser = argparse.ArgumentParser(description='Process some integers.')
parser.add_argument('integers', metavar='N', type=int, nargs='+',
                    help='an integer for the accumulator')
parser.add_argument('--sum', dest='accumulate', action='store_const',
                    const=sum, default=max,
                    help='sum the integers (default: find the max)')

args = parser.parse_args()
print(args.accumulate(args.integers))
```

## User Input During Runtime

Updated and replaced in Python 3: `raw_input()` is now `input()`.

If the prompt argument is present, it is written to standard output without a trailing newline. The function then reads a line from input, converts it to a string (stripping a trailing newline), and returns that. When EOF is read, EOFError is raised. Example:

```
<<< s = input('--> ')
>>> --> Monty Python's Flying Circus
<<< s
>>> "Monty Python's Flying Circus"
```

If the `readline` module was loaded, then `input()` will use it to provide elaborate line editing and history features.
