# Decision making
# we will ask the user questions and make decisions based on the answers

print "You enter a dark room with two doors, which door do you take?"

door = raw_input("> ")

if door == "1":
    print "there is a giant bear eating a cheesecake. What do you do?"
    print "1. Take the cheesecake"
    print "2. Scream at the bear"
    bear = raw_input("> ")
    
    if bear == "1":
        print "The bear eats your face off"
    elif bear == "2":
        print "The bear eats your legs off"
    else: print "well, doing %s is better. Bear runs off" % bear

elif door == "2":
    print "You stare at the abyss into cthulhu's retina"
    print "1. Blueberries"
    print "2. Yellow jacket clothespins"
    print "3. Understanding revolvers yelling melodies"
    
    insanity = raw_input("> ")
    if insanity == "1" or insanity == "2":
        print "You survive"
    else: print "You die"
else: print "You stumble around and die"

    
    
