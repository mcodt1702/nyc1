
#10.2 Write a program to read through the mbox-short.txt and figure out
#the distribution by hour of the day for each of the messages.
#You can pull the hour out from the 'From ' line by finding the time
#and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts,
#sorted by hour as shown below.


tabu = dict()
texto = open('mbox.txt')



for palabras in texto:
    if not palabras.startswith('From'): continue
    lector = palabras.split()


    try:
        hora = lector[5]
        #print(hora)
        delimiter = ':'
        hora2 = hora.split(delimiter)
        #print(hora2[0])
        horaexac = hora2[0]
        tabu[horaexac] = tabu.get(horaexac,0) + 1


    except:
        continue

list = list()

for key,value in tabu.items() :
	list.append((key,value))
list.sort()

for hour,count in list :
	print(hour, count)
