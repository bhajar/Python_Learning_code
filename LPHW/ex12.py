# we can also put prompts inside a raw_input 

age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you are %r old, %r tall and %r heavy" % (
age, height, weight)