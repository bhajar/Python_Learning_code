# Parameters, unpacking, variables
# A new way to pass variables to scripts 

from sys import argv

script, first, second, third = argv # all these are mapped to argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

# using import we add features to our script from the python feature set
# argv is the argument variable which holds arguments we pass to the script
# when we run it. 
