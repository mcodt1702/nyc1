
start = False
while True:
    action = input('>').lower()
    if action == 'help':
        print('''
Start - to start the car
stop - to stop the car
quit - to exit''')
    elif action == 'start':
        if start:
            print('car is already started')
        else:
            start = True
            print('car started')


    elif action == 'stop':
        if not start:
            print('car already stopped')
        else:
            start = False
            print('car stoped')

    elif action == 'quit':
        break

    else:
        print("I don't understand")
