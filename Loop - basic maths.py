# basis maths by for loop

# addition of items in list
list = [0,1,2,3,4,5,6,7,8,9]
total = 0
for list_number in list:
    total = total + list_number
print (total)

# variable can set to range

list2 = range(0,50)   # set variable with range (0,50)
print (list2)


# multiplication of items in range

list3 = range(1,5)
total2 = 1
for list2number in list3 :
    total2 = total2 * list2number
print (total2)

# multiplication and addition of each number which is multiple of 3 - range (1,50)

list4 = range(1,10)
sum = 0
mul = 1
for list4number in list4:
    if list4number % 3 == 0:
        sum = sum + list4number
        mul = mul * list4number
print ('sum of addition 3 in list4 is %d'%sum)
print ('sum of multiple 3 in list4 is %d'%mul)