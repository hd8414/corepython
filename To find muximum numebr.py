# Program to find Maximum number from 3 number

number_1 = int(input('Enter 1st number :'))
number_2 = int(input('Enter 2nd number :'))
number_3 = int(input('Enter 3rd number :'))

if number_1 > number_2:
    if number_1 > number_3:
        print ('1st number with value %d is maximum number out of three number'%number_1)
    else:
        print ('3rd number with value %d is maximum number out of three number'%number_3)

else:
    if number_2 > number_3:
        print ('2nd number with value %d is maximum number out of three number'%number_2)
    else:
        print ('3rd number with value %d is maximum number out of three number'%number_3)
