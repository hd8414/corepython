'''Program to print greeting for input time
6:00 to 12:00 - morning time
12:00 to 17:00 - afternoon time
17:00 to 20:00 - evening time
20:00 to 24:00 - night time
'''

time = int(input('what\'s the time : ' )) # define variable time to ask user to enter time

if time >= 6 and time < 12:
    print('Good morning')
elif time >= 12 and time < 17:
    print ('Good afternoon ')
elif time >= 17 and time < 20:
    print ('Good evening')
elif time >= 20 and time <= 24:
    print ('Good night')
else :
    print ('please enter valid value')