class Hero:
    def __init__(self, name):
        self.__name = name
    def _magic(self, magic):
        self.magic = magic
    def _magic1(self, magic2):
        self.magic2 = magic2
    def _magic3(self, magic4):
        self.magic4 = magic4


    def setName(self, name):
        self.__name = name


    def getName(self):
        return self.__name



p = Hero('Avatar')
p.name = f'Avatar: fire, water, air'
print(p.name)


p.setName('Avatar')
print(p.getName())
print(p._Hero__name)
