tel= input("whats your number:  ")
in_leter = {'1':'one', '2':'two', '3':'three', '4':'four', '5':'five'}

output = ''
for ch in tel:
    output += in_leter.get(ch, '!!!!') + ' '

print(output)
