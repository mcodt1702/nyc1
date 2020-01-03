padron = {}
padron['marco'] = 47, 48
#print(padron)

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
#print(f"Original position: {alien_0['x_position']}")

if alien_0['speed'] == 'slow':
    x_increment = 1

elif alien_0['speed'] == 'medium':
    x_increment = 2

else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment
#print(f"New Position: {alien_0['x_position']}")


person = {'first_name' : 'Marco', 'last_name': 'Coronado', 'age': 47, 'city': 'NY'}
#print(person['first_name'])
#print(person['city'])


for key in person.keys():
    print(f"key: {key}")
    #print(f'{key.title()} ')
