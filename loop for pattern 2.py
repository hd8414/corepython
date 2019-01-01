# program to get output of pattern 2

for raw in range(0,7):
    for col in range(0,7):
        if raw==0 or raw==3 or raw==6 or (col==0 and raw>=3 and raw<=6) or (col==6 and raw>=0 and raw<=3):
            print('*',end=' ')
        else:
            print(end='  ')
    print ('')
print('')