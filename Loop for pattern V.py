i=0
j=8
for row in range(10):
    for col in range(10):
        if (row==col and col<5):
            print('*',end=' ')
        elif((row==i and col==j) and col>4 and row<6):
            print ('*',end=' ')
            i=i+1
            j=j-1
        else:
            print(end='  ')
    print('')
print('')

