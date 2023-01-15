from sys import argv
from os.path import exists

script, from_file, to_file = argv

#we could do these two on line too, how?
to_file = open(from_file, 'w')

#Before refactoring this file to single line reduction
# from sys import argv
# from os.path import exists
#
# script, from_file, to_file = argv
#
# print("Copying from %s to %s" % (from_file, to_file))
#
# #we could do these two on line too, how?
# in_file = open(from_file)
# indata = open(from_file).read()
#
# print("The input file is %d bytes long" % len(indata))
#
# print("Does the output file exist? %r" % exists(to_file))
# print("Ready, hit RETURN to continue, CTRL-C to abort")
# input()
#
# out_file = open(to_file, 'w')
# out_file.write(indata)
#
# print("Alright, all done")
#
# #it turns out you only have to close a file after writing to it according to Google
# #I imagine this is because without the file closing the file continues to process and running in the background
# #another reason, in an analogy, writing to file without closing is like playing Pokemon without clicking save -- no mas progress muchacho
# out_file.close()
# in_file.close()
