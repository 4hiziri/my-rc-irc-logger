import socket


class rc_connection:
    def __init__(self, server, port=6667):
        self.server = server
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connect(self):
        self.sock.connect((self.server, self.port))

    def send(self, command):
        self.sock.send(command + '\n')

    def join(self, channel):
        self.channel = channel
        self.send('JOIN {}'.format(channel))

    def login(self,
              username,
              nickname,
              password=None,
              realname=None,
              hostname='localhost',
              servername='* :'):
        if realname is None:
            realname = username
        cmd = "USER {} {} {} {}\n".format(username,
                                          hostname,
                                          servername,
                                          realname)
        self.send(cmd)
        self.send('NICK {}'.format(nickname))
