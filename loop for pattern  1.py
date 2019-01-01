# program to get output of pattern 1

for raw in range (5):
    for col in range(3):
        if col==1 or raw==4 or (col==0 and raw==1):
            print('*',end=' ')
        else :
            print(end='  ')
    print('')
print ('')