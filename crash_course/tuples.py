buffet_items = ('corn', 'beans', 'lettuce', 'rice', 'brocolly')
print(buffet_items)
for items in buffet_items:
    print(items)



buffet_items = ('corn', 'mac', 'eggs', 'rice', 'brocolly')
print(buffet_items)

requested_item = 'eggs'

if requested_item in buffet_items:
    print(f'we have your item  {requested_item}')

else:
    print(f'Sorry {requested_item} is not available')
