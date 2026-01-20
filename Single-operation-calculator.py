# Single operation Calculator
a= "a"
b= "b"
c= "c"
d= "d"
e= "e"

print("Add:a \nSubtract:b \nMultiply:c \nDivide:d \nPower:e \n\n")

D1= float( input('1st Digit:'))
Operation= (input('Enter Operation:'))
D2= float( input('2nd Digit:'))

if (Operation== a):
    print(D1+D2)
elif (Operation==b):
    print(D1-D2)
elif (Operation==c):
    print(D1*D2)
elif (Operation==d):
    print(D1/D2)
elif(Operation==e):
    print(D1**D2)
else:
    print("Invalid Operation")