for row in range (7):
    for col in range (7):
        if ((col==0 or col==4) and row>0 and row<4) or ((row==0 or row==4 ) and col>0 and col<4 )or (row==col and col>2 and col<6):
            print('*',end=' ')
        else:
            print(end='  ')
    print (' ')
print (' ')