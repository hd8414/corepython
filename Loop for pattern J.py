for row in range (7):
    for col in range(7):
        if col==3 or row==0 or (row==6 and col<4) or (col==0 and row>3):
            print('*',end=' ')
        else:
            print(end='  ')
    print('')
print(' ')