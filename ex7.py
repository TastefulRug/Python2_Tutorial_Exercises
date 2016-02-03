# Prints a string
print "Mary had a little lamb."
print "Its fleece was white as %s." % 'snow' #format string, inserts values into a string
print "And everywhere that Mary went."
print "." * 10 # What'd that do? --It made 10 periods in a row
# A bunch of variables assigned
end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# Watch that comma at the end. Try removing it to see what happens.
print end1 + end2 + end3 + end4 + end5 + end6, # Concatonates variables and prints them
# The comma joins the two print lines on the same line, with a space between them
print end7 + end8 + end9 + end10 + end11 + end12

# Errors made: 
#	forgot single quotes around 'snow'
#	mistyped end10 as emd10