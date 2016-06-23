# Functions can return something

def add(a, b):
    print "Adding %d and %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "Subtracting %d from %d" % (b, a)
    return a - b
    
def multiply(a, b):
    print "Multiplying %d and %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "Dividing %d from %d" % (a, b)
    return a/b
    

print "Doing math from functions"
age = add(30, 5)
height = subtract(78, 6)
weight = multiply(80, 1)
iq = divide(100, 1)

print "Age: %d, Height: %d, Weight: %d, iq: %d" % (age, height, weight, iq)

print "A puzzle for extra credit"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes:", what, "Can you do it by hand?"


