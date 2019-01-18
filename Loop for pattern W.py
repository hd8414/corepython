i=0
j=8
for row in range(9):
    for col in range(9):
        if(row==col):
            print('*',end=' ')
        elif(row==i and col==j):
            print('*',end=' ')
            i=i+1
            j=j-1
        else:
            print(end='  ')
    print('')
print('')