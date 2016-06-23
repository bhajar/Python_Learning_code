# Reading and writing files
# we will use functions to make a simple text editor

from sys import argv

script, filename = argv

print "We're going to erase %r" % filename
print "If you don't want that, press ctrl + c(^C)"
print "If you want that, press return"

raw_input("?")

print "Opening the file..."
target = open(filename, "w") # used a w with open for writing
# use r for reading, a for append, and others

print "Truncating the file"

print "Now, I am going to ask you for 3 lines"

line1 = raw_input()
line2 = raw_input()
line3 = raw_input()

print "Going to write these into the file"

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, we close it"

target.close()
