# '/usr/share/dict/words'
# The above path is the dictionary of words that your computer uses


def get_words():
    """Function that reads all the words your machine is aware of and writes
    any word more than 3 characters to a new file
    """

    with open('/usr/share/dict/words', 'r') as rf:
        # The `with` keyword is useful for providing file data as context
        with open('./assets/words.txt', 'w') as wf:
            for line in rf:
                if len(line) > 7:
                    wf.write(line)


def get_non_exists():
    """Function that demonstrates the usefulness of try/except/finally
    and exception handling in Python
    """
    try:
        # print('I ran second')
        with open('somefile.blarp', 'r') as f:
            print(f.read())
    except (FileNotFoundError, TypeError)as e:
        print(e)

    finally:
        print('I ran last, regardless of success or failure.')


def get_binary():
    """Function that reads and exposes binary data from file.
    Useful for showing the different modes of opening a file for read/write & encoding
    """
    with open('./assets/text.txt', 'rb') as f:
        print(f.read())

def dig_hole():
    print('dig dug')

print('__name__', __name__)

if __name__ == '__main__':
    dig_hole()
    1 / 0
    get_words() 
    get_non_exists()
    get_binary()
