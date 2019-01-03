for row in range(0,6):
    for col in range(0,6):
        if row==col and col>2:
            print('*',end='  ')
        else:
            print (end='   ')
    print('')
print('')