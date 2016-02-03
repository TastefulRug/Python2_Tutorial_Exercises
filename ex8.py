# Create a variable with 4 repr string formatters
formatter = "%r %r %r %r"

# echos the formatter variable with 1 2 3 4 replacin the %r's
print formatter % (1, 2, 3, 4,)

# echo the four strings in single quptes
print formatter % ("one", "two", "three", "four")

# echo the True and False values without quotes because they're boolean and not really strings
print formatter % (True, False, False, True)

# echo the literal contents of the formatter variable 4 times
print formatter % (formatter, formatter, formatter, formatter)

# echo the four lines and join them together in one line/string
print formatter % (
	"I had this thing.",
	"That you could type up right.",
	# This string has a ['] in it so it's contained in double quotes
	"But it didn't sing.", # Rest of the strings are all single quotes
	"So I said goodnight."
) # Close the parenthesis block

# Again, %r is for raw info for debugging, %s is for actual use
# No errors this time