from enum import Enum

class TypeService():
    NEW = 'New'
    UNCOMMON = 'Uncommon'
    COMMON = 'Common'

    def __init__(self) -> None:
        super().__init__()
        with open('uncommonPorts') as unport:
            self.uncommonPorts = [port.strip() for port in unport.readlines()]

    def type(self, port):       
        if str(port) in self.uncommonPorts:
            return self.UNCOMMON
        return self.COMMON

class Repository():
    
    def __init__(self, ddbb) -> None:
        self._ddbb = ddbb
        self.connect()        

    def connect(self):
        with open(self._ddbb,'r') as services:
            self.services = [service.strip() for service in services.readlines()]

    def is_new_service(self, ip, port, protocol):
        return f"{ip} {port}/{protocol}" not in self.services

    def add_new_service(self, ip, port, protocol):
        with open(self._ddbb,'a') as services:
            service = f"{ip} {port}/{protocol}"
            services.write(service + "\n")
            self.services.append(service)



repo = Repository('ddbb')

# print(repo.is_new_service('2.2.2.2','333','tcp'))
# print(repo.is_new_service('2.2.2.2','444','tcp'))
# print(repo.add_new_service('2.2.2.2','333','tcp'))
# print(repo.is_new_service('2.2.2.2','333','tcp'))

# ts = TypeService()
# print(ts.uncommonPorts)
# print(ts.type('23'))
# print(ts.COMMON)
