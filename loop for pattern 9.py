for row in range(7):
    for col in range(7):
        if row==6 or row==3 or row== 0 or col==6 or(col==0 and row>=0 and row<=3):
            print('*',end=' ')
        else:
            print(end='  ')
    print ('')
print('')