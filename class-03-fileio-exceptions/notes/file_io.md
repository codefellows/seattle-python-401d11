# Reading and Writing Files

## What are files?
Python understands 'Files' slightly different than other media.

For example, in Windows OS a file can be any item edited, created, or manipulated by the user/OS, which means that files can be executables, plain text, images, or almost any other type. Most files are organized by a file directory structure managed by the OS.

Python recognizes files in a different way; a file is either categorized as text or binary. The distinction between the two is an important factor in handling file I/O.

Text files are structured as a sequence of lines, where each line includes a sequence of characters. This is what you know as code or syntax. Each line is terminated with a special character, called the EOL or End of Line character. There are several types, but the most common is the comma {,} or newline character. It ends the current line and tells the interpreter a new one has begun.

A backslash character can also be used, and it tells the interpreter that the next character – following the slash – should be treated as a new line. This character is useful when you don’t want to start a new line in the text itself but in the code.

A binary file is any type of file that is not a text file. Because of their nature, binary files can only be processed by an application that know or understand the file’s structure. In other words, they must be applications that can read and interpret binary.

## Reading files
Opening a file in Python is a fairly simple expression, as shown below:
```txt
<!-- text.txt -->
hello I am a text file
```

```python
f = open('text.txt', 'r')  # -r flag is for read-only mode
print(f.read())
# hello I am a text file
```

In addition to reading the whole file, you can utilize a loop and file methods to read one line at a time.
```txt
Hello
I am a text file
```
```python
f = open('text.txt', 'r')
for line in f:
    print(line)
f.close()  # It's always a good practice to explicitly `close()` the file when operations are complete.
# Hello
# I am a text file
```

You also have a cleaner interface through the language, and a more practical approach which allows Exception handling via the `with` keyword!
```txt
Hello world!
I was read using the with keyword.
```
```python
with open('text.txt', 'r') as f:
    try:
        for line in f:
            print(line)
    except FileNotFoundError:
        print('There was an error locating the file resource')
# Not necessary to 'close()' a file when using 'with' as it happens automatically
```

## Writing files
While reading file contents is a handy way to get data from a file system, it's also a necessity that the ability to write data to a file is provide by the language. In Python, once a file has been targeted by the `open()` function, it can be further configured to write data back to a file.
```python
# `text.txt` does not currently exist in this example, and will be created.
with open('text.txt', 'w') as f:
    f.write('Hello world! I was just written to the file\n')
```
```txt
'Hello world! I was just written to the file\n'
```
