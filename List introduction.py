# empty list
animals = [ ]
print (animals)

# list with items
animals1 = ['dog', 'cat', 'monkey']
print (animals1)

# indexing in list
print (animals1[0])

# list with mix type of elements
list = [10, 10.5, 'hardik', 25.52]
print (list)

# nesting in list
list2 = [[10,20],[30,40],[50,60]]
print (list2[2])
print (list2[1][0]) # 1st element on second list

# example of list

for num in [100,200,300,400]:
    print (num)

print ( )

'''************************************************************************'''

''' LIST OPERATION '''
# REPLACE
list3 = [5,15,25,35]
list3[2] = 3.7
print(list3)
print ()

# INSERT
list3.insert(2,'hello')
print(list3)
print ()

# SORT - LIST HAS TO HAVE SAME ELEMENTS
animal = ['dog','cat','monkey']
animal.sort()
print(animal)
list4 = [49,29,9,39,19]
list4.sort()
print(list4)

# delete element
del list4[2] # deleting single element
print (list4)
del list4 # deleting full list

# APPEND
animal.append('donkey')
print (animal)

# REVERSE
animal.reverse()
print(animal)

# example 2
fruits = ['apple','banana']
print(fruits)

fruits[1] = 'grapes' # replace
print (fruits)

fruits.insert(1,'orange')   # insert
print(fruits)

fruits.sort()
print(fruits)               # sort

del fruits[0]
print (fruits)              # delete

fruits.append('cherry')
print(fruits)               # append

fruits.reverse()            # reverse

x = fruits.index('orange')
print (x)                   #index

fruits.pop(2)
print(fruits)               #pop

fruits.remove('cherry')
print (fruits)              # remove

fruits.clear()
print (fruits)               #clear


# extend list

fruits2 = ['apple', 'banana', 'cherry']
cars = ['Ford', 'BMW', 'Volvo']

fruits2.extend(cars)         # extend
print(fruits2)

