''' introduction to dictionary

dic = {'KEY' : 'VALUE' , 'KEY1' : 'VALUE1'}
print(dic)
no indexing on dic.
'''

room_items = {'tv':'samsung', 'fan':'usha','laptop':'hp'}
print (room_items)

# copying dic.
x=dict.copy(room_items)
print (x)

# use of fromkey
items = ['tv', 'fan','laptop']
company = ['samsung','usha','hp']
room_items2 = dict.fromkeys(items,company)
print (room_items2)

# get method
print (room_items.get('tv'))
print (room_items.get('fan'))
x1 = room_items.get('tv')
print (x1)

# print items on dic
ab=room_items.items()
print (ab)

# print keys of dic.
cd=room_items.keys()
print (cd)

# remove specific element
ef=room_items.pop('laptop')
print (ef)
print (room_items)

# add elements on dic.
room_items.update({'phone' : 'iphone'})
print (room_items)
room_items.setdefault('light','phillips')
print(room_items)

# remove last item from dic
gh = room_items.popitem()
print (gh)
print (room_items)

# print value of dic
x2 = room_items.values()
print (x2)


