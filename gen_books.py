#!/usr/bin/env python
# Interactive bible book generator
from esv_session import ESVSession
import sys

def generateBook(book):
	while book != 'quit':
	    filename = raw_input('Output filename: ')
	    index = 1
	    outfile = open(filename, 'w')
	    while True:
	      result = bible.doPassageQuery(book + str(index))
	      if result == errormsg:
	        print 'Successfully finished writing file. Closing...'
	        outfile.close()
	        break
	      else:
	        outfile.write(result)
	        index += 1
	    passage = raw_input('Enter book: ')


print "Welcome to the ESV Bible passage lookup tool."
print "Enter a book to compile: (e.g. eph)"

try:
    key = sys.argv[1]
except IndexError:
    key = 'IP'
bible = ESVSession(key)
errormsg = 'ERROR: No passage found for your query.'
book = raw_input('Enter book: ')
generateBook(book)
