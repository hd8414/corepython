# program to find minimum number out of three number

number_1 = float(input('Enter 1st number :'))
number_2 = float(input('Enter 2nd number :'))
number_3 = float(input('Enter 3rd number :'))

if number_1 < number_2:
    if number_1 < number_3:
        print('1st number is minimum with value %.2f out of three number'%number_1)
    else:
        print('3rd number is minimum with value %.2f out of three number' % number_3)
else:
    if number_2 < number_3:
        print('2nd number is minimum with value %.2f out of three number'%number_2)
    else:
        print('3rd number is minimum with value %.2f out of three number' % number_3)