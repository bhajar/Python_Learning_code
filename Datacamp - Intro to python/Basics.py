print(5 / 8)

print(7 + 10)

# print works differently from python 2 as it is a function in python 3

# ** gives exponential; % gives remainder
# Addition and subtraction
print(5 + 5)
print(5 - 5)

# Multiplication and division
print(3 * 5)
print(10 / 2)

# Exponentiation
print(4 ** 2)

# Modulo
print(18 % 7)

# How much is your $100 worth after 7 years if invested at 10%?
print(100 * (1.1**7)) 


# Video on variables and types
# Defining a variable. same height and weight as LPHW

height = 1.82
weight = 82
BMI = weight/height**2
BMI
type(BMI) # types are str, bool(boolean), int, float

savings = 100
print(savings)

factor = 1.1
result = savings * factor**7
print(result)

# create more variables
# Create a variable desc
desc = "compound interest"

# Create a variable profitable
profitable = True
type(profitable)
print("great" + "game")

# Several variables to experiment with
savings = 100
factor = 1.1
desc = "compound interest"

# Assign product of factor and savings to year1
year1 = factor * savings

# Print the type of year1
type(year1)

# Assign sum of desc and desc to doubledesc
doubledesc = desc + desc

# Print out doubledesc
print(doubledesc)

# Definition of savings and result
savings = 100
result = 100 * 1.10 ** 7

# if we need to convert something to a string, it can be done using str()
# Fix the printout
print("I started with $" + savings + " and now have $" + result + ". Awesome!")
print("I started with $" + str(savings) + " and now have $" + str(result) + ". Awesome!")

# Definition of pi_string
pi_string = "3.1415926"

# Convert pi_string into float: pi_float
type(pi_string)
pi_string = float(pi_string)
















