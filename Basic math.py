# program to do simple maths of two value

a = float(input('enter value of a :'))
b = float(input('enter value of b :'))
c = a+b
d = a-b
e = a*b
f = a/b
g = a%b
h = a**b

print ('sum of a and b = %.f'%c)
print ('sub of a and b = %.2f'%d)
print ('multi of a and b = %.3f'%e)
print ('div of a by b = %.1f'%f)
print ('mod of a by a = %.2f'%g)
print ('power of a of b = %.2f'%h)

x = int(input('enter value of x :'))
y = int(input('enter value of y :'))

i,j,k,l,m,n = x+y,x-y,x*y,x/y,x%y,x**y # multiple variable can define in 1 line

print ('sum of x and y = %.f'%i)
print ('sub of x and y = %.2f'%j)
print ('multi of x and y = %.3f'%k)
print ('div of x by y = %.1f'%l)
print ('mod of x by y = %.2f'%m)
print ('power of x of y = %.2f'%n)