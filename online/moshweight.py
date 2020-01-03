w = int(input('what is your weight?    '))
units = input('Is your weight in Lbs (L) or is it in Kilos (k)   ')

if units.upper() == 'K':
    weight = (w) * 2.20
    print('Your weight is', weight ,'pounds')

else:
    weight = (w) / 2.20
    print('Your weight is', weight ,'kilos')
