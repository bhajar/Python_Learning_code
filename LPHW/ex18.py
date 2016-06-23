# Names, variables, code, functions

# Functions can be created by using def
# We will make 4 functions that are related

# This is like the scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print "arg1: %r, arg2: %r" % (arg1, arg2)
    
# So, that *args is quite pointless
    
def print_two_again(arg1, arg2):
    print "arg1: %r, arg2: %r" % (arg1, arg2)

# This takes just one argument
def print_one(arg1):
    print "arg1: %r" % arg1
    
# This takes no arguments 
def print_none():
    print "I got nothing"
    

print_two("one", "two")
print_two_again("one", "two")
print_one("one")
print_none()


#from pydoc import help
#help(open)