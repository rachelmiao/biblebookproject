# Generates specified book in specified version
# List of versions found at getbible.net/api
# Script usage: python gen_book_by_version.py [book] [version]
# Written by Rachel Miao

import sys
import urllib, json
from optparse import OptionParser

def main():
  parser = OptionParser()
  parser.add_option('-n', '--newlines', action='store_true', dest='newlines',
                    help='Whether to have line breaks after every verse')
  (options, args) = parser.parse_args()

  if len(args) != 2:
    print len(args)
    print 'ERROR: Incorrect number of arguments'
    print 'Usage: python gen_book_by_version.py [book] [version]'
    quit()

  book = args[0].lower()
  version = args[1].lower()
  filename = book + '_' + version + '.txt'

  print 'Generating the book of ' + book + ' in the version ' + version
  print 'Output file: ' + filename

  outfile = open(filename, 'w+')
  url = 'https://getbible.net/json?p=' + book + '&lang=' + version
  jsonString = urllib.urlopen(url).read()[1:-2]  # weird json formatting in url
  data = json.loads(jsonString)
  chapters = data['book']

  for i in range(len(chapters)):
    # New chapter
    outfile.write('\n\n' + book.title() + ' ' + str(i+1) + '\n\n')  # chapter heading
    verses = chapters[str(i+1)]['chapter']
    for j in range(len(verses)):
      verse = verses[str(j+1)]['verse']

      # We need to treat ascii and non-ascii files differently
      try:
        verse.encode('ascii')
      except UnicodeError:
        # not ascii
        verse = verse.encode('utf-8')

        # chinese scripts have extra spacing, so remove
        if version == 'cus' or version == 'cns':
          verse = verse.replace(' ', '')
          verse = verse.strip()
      
      if options.newlines == True:
        verse = verse + '\n'
      outfile.write('%s' % verse)

  print 'Success! Goodbye.'
  outfile.close()

if __name__ == '__main__':
  main()