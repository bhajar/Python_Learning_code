# reading files
# Everything we learnt about argv and raw_input is so that we can learn to read files

# we want to ask the user to open a file and print the contents

from sys import argv

script, filename = argv

txt = open(filename) # a built in function. the preferred way to open a file

print "Here is your file %r:" % filename
print txt.read() # we call a function on txt

# the file is txt and using a dot(.) we give a command
# the parameters are given inside the ()

print "type the filename again:"
file_again = raw_input("> ")

txt_again = open(file_again)

print txt_again.read()

