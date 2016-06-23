formatter = "%r %r %r %r"

print formatter % (1, 2, 3, 4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, True, False)
print formatter % (formatter, formatter, formatter, formatter) # takes it as character
print formatter % (
"I had this thing.",
"That you could type up right,",
"But it didn;t sing.",
"So I said good night."
)
# we use %r while debugging information about something only. 
# Use %s for displaying
