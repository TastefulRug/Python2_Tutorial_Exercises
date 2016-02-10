from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "Copying from %s to %s" % ( from_file, to_file)

# we could do these two one line, how?
# in_file = open(from_file)
indata = open(from_file).read()

print "The inputfile is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
# in_file.close()

# Errors:
# Didn't type the s on the end of exists

# The encoding of the test.txt was weird, such that lines were replaced
# with a bunch of chinese characters. Manually changing the file's encoding
# fixed things.
# Learn how to do encoding/decoding in Python later.