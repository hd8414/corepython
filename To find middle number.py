# Program to find middle number out of three number

number_1 = int(input('Enter 1st number :'))
number_2 = int(input('Enter 2nd number :'))
number_3 = int(input('Enter 3rd number :'))

'''if number_1 == number_2:
    print('input incorrect as 1st and 2nd numbers are similar')
if number_2 == number_3:
    print('input incorrect as 2nd and 3rd numbers are similar')
if number_3 == number_1:
    print('input incorrect as 3rd and 1st numbers are similar')
'''
if number_1 > number_2:
    if number_1 < number_3:
        print('1st number with value %d is middle number out of three'%number_1)
    elif number_1 > number_3:
        if number_3 > number_2:
            print ('2nd number with value %d is middle number out of three'%number_2)
        elif number_3 < number_2:
            print ('2nd number with value %d is middle number out of three' % number_3)


