game_played = input("Do you want to play 'aliens', stages? or fruits?   ")
if game_played == 'aliens':

    alien_color = input("What color was the alien you shot??   ")
    p = 0

    if alien_color == 'green':
        print('you got 10 point')
        p = p + 10

    elif alien_color == 'blue':
        print("You got 20 points")
        p = p + 20

    elif alien_color == 'red':
        print("you got 40 points")
        p = p + 40

    elif alien_color == 'white':
        print('You killed your best friend')
        p = 0
    print(f'Your total points are {p}')

if game_played == "stages":

    age = int(input("Tell me how old are you and I'll tell you which stage you're on."))

    if age < 2 :
        print ( "You are a Baby" )

    elif age < 4:
        print ( 'You are a toddler' )

    elif age < 13:
        print ( 'Youre a kid' )

    elif age < 20:
        print ( 'Youre a teenage dirt bag' )


    elif age < 65:
        print ( "you're and adult, act like one!!!  " )

    elif age >= 65:
        print ( 'youre a respected elder' )

else:

    fruits = ['banana', 'apple', 'orange', 'kiwi']

    fruit = input(' what fruit do you like?   ')

    if fruit in fruits:
        print('I know what you like!!')
        
    else:
        print("sorry we dont have it")



