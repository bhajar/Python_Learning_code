# More files

# We'll write a script to copy one file to another

from sys import argv
from os.path import exists 

script, from_file, to_file = argv

print "Copying from %s to %s" %(from_file, to_file)

# These two can be done on one line too 
in_file = open(from_file)
indata = in_file.read()

print "The input data is %d bytes long" % len(indata)

print "Does the output file really exist? %r" % exists(to_file)
# returns true if file exists
# we imported this function from os.path

print "hit return to continue, ctrl + c to abort"
raw_input()

out_file = open(to_file, "w")
out_file.write(indata)
print "All right, done"

out_file.close()
in_file.close()

