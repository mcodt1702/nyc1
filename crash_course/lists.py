novios = ['Marco', 'Hernan', 'Mario','Gustavo', 'Kino', 'Samuel']
print(len(novios) -1)

novios.append('victor')
print(novios)
del novios[-1]
print(novios)
novios.insert(3, 'kevin')
print(novios)
del(novios[3])
ultimo = novios.pop()
print(ultimo)
print(novios)

print(f'{novios[2]} me gustaria invitarte a cenar')
print(f'{novios[3]} me gustaria invitarte a cenar')
print(f'{novios[4]} me gustaria invitarte a cenar')
print(f'{novios[0]} me gustaria invitarte a cenar')
novios.append('Samuel')
novios.reverse()
print(novios)
novios.sort()
print(novios )


