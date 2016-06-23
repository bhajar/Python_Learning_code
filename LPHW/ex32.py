# Loops and lists

the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quaters']

# This first kind of for loop runs through a list

for number in the_count:
    print "This is %d count" % number
    
# same as above
    
for fruit in fruits:
    print "A fruit of type %s" % fruit

# also, we can go through mixed lists
# we have to use %r as we don't know what's in it

for i in change:
    print "i got %r" % i
    
# we can also start with empty lists and do operations on them
    
elements = []

for i in range(0, 6):
    print "adding %d to the list" % i
    # lists understand the function append
    elements.append(i)
    print "%r" % elements

# we can print them out too
for i in elements:
    print "Element was %d" % i


range(1, 7) # range does not include the last number