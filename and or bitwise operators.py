a=12.5
b=-3.7
c=9

print((a>b) and (b==c))
#True and False
#output:
#False

print((a<=c) or (b!=a))
#False or True
#output:
#True

print((a>c) or (c!=b))
#True or True
#output:
#True

print((a==c) and (b>=c))
#False and False
#output:
#False

print(a and b)
#output:
#-3.7

print(a or c)
#output:
#12.5

print((b or c)+(a and b))
#-3.7+(-3.7)
#output:
#-7.4

a=2
b=3

print((a|b)/(a&b))
#3/2
#output:
#1.5

print((~b) and (~a))
#-4 and -3
#output:
#-3

print((a>>2) or (b<<1))
#output:
#6

