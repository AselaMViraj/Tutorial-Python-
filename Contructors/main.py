class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    def draw(self):
        print("draw")


p1 = Point(10, 20)
p1.x = 25
print(p1.x)


class Person():
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f'Hi, I am {self.name}')


asela = Person("Asela")
asela.talk()