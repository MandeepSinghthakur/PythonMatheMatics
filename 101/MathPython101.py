from fractions import Fraction
a = 3 
print(a+1)

##Diffrent Kinds of Numbers
print(type(3))

print(type(3.5))

print(type(3.0))


## Working with Fractions
f = Fraction(3,4)
print(f)
f = Fraction(3,4) +1 +1.5
print(f)


#Working with Complex Numbers
a = 2 + 3j
print(type(a))

a = complex(2,3)
print(a)

 #You can operate on Complex Numbers
b = 3 +3j

print(a + b)

print(a * b)

#Print out parts of Complex Number

z = 2 + 3j
print(z.real)

print(z.imag)

# The Conjugate of a Complex Number has the same real part but an imaginary part
# with an equal magnitude and an opposite sign. It can be obtained with Conjugate Method
# available to us in Python
print(z.conjugate())


# Both real and imaginary parts are floating Point Numbers. Using the real and imaginary 
# parts , you can then calculate the magnitude of a complex number with the following formula where
# x and y are the real and imaginary numbers
# Sqaureroot of x^2 + y^2

print(pow(pow(z.real,2) + pow(z.imag, 2), 0.5))

##Handling Exceptions and Invalid input

try:
    a = float(input('Enter a number: '))
except ValueError:
    print('You entered a invalid number')


# Calculating the factors of an Integer

def is_factor(a,b):
    if b % a == 0:
        return True
    else:
        return False

print(is_factor(4,1024))


# How Range Works
for i in range(1,4):
    print(i)


#Find the Factors of an INteger

def factors(b):
    for i in range(1, b+1):
        if b % i == 0:
            print(i)

#Generating Multiplication Tables
# Consider three numbers a,b and n , where n is the integer, such that a * n = b
# We can Say that b is the nth multipple of a. e.g 4 is the 2nd multiple of 2 , and 1024 is the 512nd multiple of 52

def multi_table(a):
    for i in range(1,11):
        print('{ 0 } x { 1 } = { 2 })' .format(a, i, a*i))

#Converting Measurement Units
# DO as a Practice - Miles - Km and Celsius to fahrenheit

#FINDING THE ROOTS OF QUADRATIC EQUATION
def roots(a,b,c):
     D = pow((b*b - 4*a*c),0.5)
     x_1 = (-b + D)/(2*a)
     x_2 = (-b-D)/(2*a)
     print('x1: {0}'.format(x_1))
     print('x2: {0}'.format(x_2))
    

