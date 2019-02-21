import struct


class Bitmap(object):
    def __init__(self, file_data):
        """Initialization method for Bitmap instance.
        Provides itemized data related to consumed Bitmap file through the use of a MemoryView object.
        """
        self.source = bytearray(file_data)
        self.memory_view = memoryview(self.source)

        self.offset = struct.unpack('I', self.memory_view[10:14].tobytes())[0]
        self.color_table = self.memory_view[54:self.offset]
        self.pixel_array = self.memory_view[self.offset:]

    @classmethod
    def read_file(cls, origin):
        """Class Method which consumes a file path as input, and returns a Bitmap instance.
        """
        pass

    def write_file(self, target):
        """Instance Method which accepts a target file path and writes the instance source data to target path.
        """
        pass

    def get_headers(self):
        """Instance Method which provides instance source data as readable output to std out.
        """
        import struct as s
        result = f'''
            Type: {s.unpack('I', self.memory_view[0:2].tobytes())[0]}
            Size: {s.unpack('I', self.memory_view[2:6].tobytes())[0]}
            Reserved 1: {s.unpack('H', self.memory_view[6:8].tobytes())[0]}
            Reserved 2: {s.unpack('H', self.memory_view[8:10].tobytes())[0]}
            Offset: {s.unpack('I', self.memory_view[10:14].tobytes())[0]}            
            DIB Header Size: {s.unpack('I', self.memory_view[14:18].tobytes())[0]}
            Width: {s.unpack('I', self.memory_view[18:22].tobytes())[0]}
            Height: {s.unpack('I', self.memory_view[22:26].tobytes())[0]}
            Colour Planes: {s.unpack('H', self.memory_view[26:28].tobytes())[0]}
            Bits per Pixel: {s.unpack('H', self.memory_view[28:30].tobytes())[0]}
            Compression Method: {s.unpack('I', self.memory_view[30:34].tobytes())[0]}
            Raw Image Size: {s.unpack('I', self.memory_view[34:38].tobytes())[0]}
            Horizontal Resolution: {s.unpack('I', self.memory_view[38:42].tobytes())[0]}
            Vertical Resolution: {s.unpack('I', self.memory_view[42:46].tobytes())[0]}
            Number of Colours: {s.unpack('I', self.memory_view[46:50].tobytes())[0]}
            Important Colours: {s.unpack('I', self.memory_view[50:54].tobytes())[0]}
        '''
        return result

    # TODO: Write your instance methods for transformations here as part of the Bitmap class.
