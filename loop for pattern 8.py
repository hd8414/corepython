for row in range(7):
    for col in range(7):
        if row==6 or row==3 or row== 0 or col==0 or col==6 :
            print('*',end=' ')
        else:
            print(end='  ')
    print ('')
print('')