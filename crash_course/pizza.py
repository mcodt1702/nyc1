pizzas = ['peperoni', 'margarita', 'cuatro stragioni', 'hawaian', "meat lover's"]
print(pizzas)

for pizza in pizzas:
    print(f'I love {pizza} pizza ')
print('\nI love all the pizzas you can make!!!')

print(f'the first three items of the list are {pizzas[0:3]}')
print(f'The last three items are{pizzas[-3:]}')

friend_pizzas = pizzas[:]
friend_pizzas.append('mushroom')
print(friend_pizzas)
print(pizzas)

print('\n My friens favorite pizzas: ')
for pay in pizzas:
    print(pay)
