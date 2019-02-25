import random
import uuid


class ChatClient(object):
    def __init__(self, conn=None, addr=None):
        self.id = str(uuid.uuid4())
        self.nick = 'user_{}'.format(random.random())
        self.conn = conn
        self.addr = addr
