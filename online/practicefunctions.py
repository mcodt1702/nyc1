from online import coordenatesnestesd
import random


class Person:
    def __init__(self, name):
        self.name = name

    def greet_user(self, first, last):
        print(f'Hello Mr. {last} or do you preffer {first}')

    def talk(self):
        print("otra cosa")


x = Person('Marco')
print(x.name)
x.talk()
x.greet_user('Daiel', "VIllarreal")

fran = Person('Francis')
print(fran.name)


class Dog(Person):
    pass


lolo = Dog('kylie')
lolo.greet_user('Lulu', 'Rodriguez')

numbers = [4, 2, 7, 9, 3, 11, 4, 3, 35, 0]

esigual = coordenatesnestesd.find_max(numbers)

print(esigual)


class Dice:
    def roll(self):
        first = random.randint(1, 6)
        second = random.randint(1, 6)
        return first, second


dice1 = Dice()
print(dice1.roll())




