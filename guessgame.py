
c = 0
secret_number = 9
limit = 3


while  c < limit:
    guess = int(input('Guess the right number:   '))
    c = c + 1
    if guess == secret_number:
        print('You won!!  ')
        break
    
