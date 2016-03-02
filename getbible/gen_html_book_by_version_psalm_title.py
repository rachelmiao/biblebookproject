# Generates specified book in specified version
# List of versions found at getbible.net/api
# Script usage: python gen_book_by_version.py [book] [version]
# Written by Rachel Miao

import codecs
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
  filename = book + '_' + version + '.html'

  print 'Generating the book of ' + book + ' in the version ' + version
  print 'Output file: ' + filename

  outfile = codecs.open(filename, 'w', 'utf-8')

  outfile.write('<html><meta charset="utf-8" />')
  url = 'https://getbible.net/json?p=' + book + '&lang=' + version
  jsonString = urllib.urlopen(url).read()[1:-2]  # weird json formatting in url
  data = json.loads(jsonString)
  chapters = data['book']

  for i in range(len(chapters)):
    # New chapter
    psalmsTitle = u'\u8BD7\u7BC7'
    outfile.write('<br><br><b>%s ' % psalmsTitle)
    outfile.write(str(i+1) + '</b><br><br>')  # chapter heading
    verses = chapters[str(i+1)]['chapter']
    for j in range(len(verses)):
      verse = verses[str(j+1)]['verse']
      if options.newlines == True:
        verse = verse + '<br>'
      outfile.write(verse)

  print 'Success! Goodbye.'

  outfile.close()

if __name__ == '__main__':
  main()
