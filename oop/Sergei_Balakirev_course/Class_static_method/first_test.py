class Server:
    __count_ip = 1

    def __init__(self):
        self.buffer = []
        self.IP = self.__count_ip
        self.router = None
        Server.__count_ip += 1

    def send_data(self, data):
        if self.router:
            self.router.buffer.append(data)

    def get_data(self):
        b = self.buffer[:]
        self.buffer.clear()
        return b

    def get_ip(self):
        return self.IP


class Router:

    def __init__(self):
        self.servers = {}  # Существующие сервера
        self.buffer = []  # Список принятых пакетов (объекты класса Data)

    def link(self, server):
        self.servers[server.IP] = server
        server.router = self

    def unlink(self, server):
        s = self.servers.pop(server.IP, False)
        if s:
            server.router = None

    def send_data(self):
        for i in self.buffer:
            if self.servers.get(i.IP):
                a = self.servers.get(i.IP)
                a.buffer.append(i)
        self.buffer.clear()


class Data:

    def __init__(self, data, ip):
        self.data = data
        self.IP = ip
