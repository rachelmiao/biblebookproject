#!/usr/bin/env python
from esv_session import ESVSession
import sys

books = ['Genesis','Exodus','Leviticus','Numbers','Deuteronomy','Joshua','Judges','Ruth','1Samuel','2Samuel','1Kings','2Kings','1Chronicles','2Chronicles','Ezra','Nehemiah','Esther','Job','Psalms','Proverbs','Ecclesiastes','SongofSongs','Isaiah','Jeremiah','Lamentations','Ezekiel','Daniel','Hosea','Joel','Amos','Obadiah','Jonah','Micah','Nahum','Habakkuk','Zephaniah','Haggai','Zechariah','Malachi','Matthew','Mark','Luke','John','Acts','Romans','1Corinthians','2Corinthians','Galatians','Ephesians','Philippians','Colossians','1Thessalonians','2Thessalonians','1Timothy','2Timothy','Titus','Philemon','Hebrews','James','1Peter','2Peter','1John','2John','3John','Jude','Revelation']

print "Welcome to the ESV Bible generator."

try:
    key = sys.argv[1]
except IndexError:
    key = 'IP'

bible = ESVSession(key)
errormsg = 'ERROR: No passage found for your query.'

for book in books:
    print 'Extracting ' + book
    index = 1
    outfile = open(book + '.txt', 'w')
    while True:
      result = bible.doPassageQuery(book + str(index))
      if result == errormsg:
        outfile.close()
        break
      else:
        outfile.write(result)
        index += 1
