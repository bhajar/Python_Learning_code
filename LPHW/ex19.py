# Functions and variables

# note that the variables in our functions are not related to the variables in
# our script

def cheese_and_crackers(cheese_count, boxes_of_crackers):
    print "You have %d cheese" % cheese_count
    print "You have %d boxes of crackers" % boxes_of_crackers
    print "A lot"
    print "Get a blanket"
    
print "We can give the functions numbers directly"
cheese_and_crackers(20, 30)

print "Or, we can use the variables from our scripts:"
amount_of_cheese = 10
amount_of_crackers = 50

cheese_and_crackers(amount_of_cheese, amount_of_crackers)

print "We can do math inside too"
cheese_and_crackers(10 + 20, 5 + 6)

print "And, we can combine the two, variables and math"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)

