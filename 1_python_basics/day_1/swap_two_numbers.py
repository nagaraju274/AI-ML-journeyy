#swapping two numbers with using a temparary variable
print("swapping two numbers with using a temparary variable")
a=5
b=10
print("before swapping: ")
print("a=",a)
print("b=",b)
temp=b
b=a
a=temp
print("After swapping:")
print("a=",a)
print("b=",b)

#swapping two numbers without using a temparary variable
print("swapping two nuumbers without using a temparary variable")
x=15
y=20
print("before swapping:")
print("x=",x)
print("y=",y)
x=x+y
y=x-y
x=x-y
print("After swapping: ")
print("x=",x)
print("y=",y)
