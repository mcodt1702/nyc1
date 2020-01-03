buffet_items = ('corn', 'mac', 'eggs', 'rice', 'brocolly', 'potatos', 'butter')
#print(buffet_items)

#for food in buffet_items:
 #   print(food)


item = input('what igredeint do you want??')
if item in buffet_items:
    print('we have what you want')
else:
    print('Sorry can we offer you something else?  ')

drink = input('Would you like a drink with that???   yes or no?      ')

if drink == 'yes':
    age = int(input('How old are you??? '))
    if age >= 21:
        print('We can serve all the drinks you need. Thank you')

    else:
        print('We only serve 21 and over, sorry')

else:
    print('thank you for coming!!!  ')
