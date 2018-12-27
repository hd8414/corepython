# program to swap value of two variable

a = 15
b = 20
x = 15
y = 20
# method 1 by using third variable
c = a
a = b
b = c
print (a)
print (b)

# method 2
x,y = y,x
print (x)
print (y)
