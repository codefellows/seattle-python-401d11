import cmd
import sys


class BitmapManipulator(cmd.Cmd):
    intro = 'Welcome to the bitmap manipulator.   Type help or ? to list commands.\n'
    prompt = '> '

    @staticmethod
    def do_get_headers(source):
        """
        To use this type 'get_headers' followed by the file location's source.

        get_headers <source>

        Returns a line-item response of the file's header data.
        """
        pass

    def do_transform(self, arg):
        """
        To use this type in 'transform' followed by
        the original file location and the new file location
        and the type of change you would like to do.

        transform <original> <new> <transform>

        Creates a new file at 'new' location with the provided 'transform' applied to the new file.
        """
        pass

    @staticmethod
    def do_exit(args):
        """
        To use this type in 'exit' and the CLI tool will cleanly exit the running application.
        """
        sys.exit()


if __name__ == '__main__':
    BitmapManipulator().cmdloop()


