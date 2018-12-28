# Program to find middle number out of three number

number_1 = int(input('Enter 1st number :'))
number_2 = int(input('Enter 2nd number :'))
number_3 = int(input('Enter 3rd number :'))

if number_1 < number_2 and number_2 < number_3:
    print('2nd number with value %d is middle number out of three number'%number_2)
elif number_1 > number_2 and number_1 < number_3:
    print('1st number with value %d is middle number out of three number'%number_1)
elif number_3 < number_2 and number_3 > number_1:
    print('3rd number with value %d is middle number out of three number'%number_3)
else:
    if number_1 == number_2 and number_1 != number_3 and number_2 != number_3:
        print('input is incorrect as 1st and 2nd numbers are same with value %d'%number_1)
    elif number_2 == number_3 and number_2 != number_1 and number_1 != number_3:
        print('input is incorrect as 2nd and 3rd numbers are same with value %d'%number_2)
    elif number_1 == number_3 and number_1 != number_2 and number_2 != number_3:
        print('input is incorrect as 1st and 3rd numbers are same with value %d'%number_1)
    elif number_1 == number_2 == number_3 :
        print('input incorrect as entered value %d of all three numbers are same'%number_1)