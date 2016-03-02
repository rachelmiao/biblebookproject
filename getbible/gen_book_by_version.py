# Generates specified book in specified version
# List of versions found at getbible.net/api
# Script usage: python gen_book_by_version.py [book] [version]
# Written by Rachel Miao

import sys
import urllib, json

def main():
  if (len(sys.argv) < 3):
    print 'ERROR: Not enough arguments'
    print 'Usage: python gen_book_by_version.py [book] [version]'
    quit()

  book = sys.argv[1].lower()
  version = sys.argv[2].lower()
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
    outfile.write('\n' + book.title() + ' ' + str(i+1) + '\n\n')  # chapter heading
    verses = chapters[str(i+1)]['chapter']
    for j in range(len(verses)):
      raw = verses[str(j+1)]['verse']

      # We need to treat ascii and non-ascii files differently
      try:
        raw.encode('ascii')
      except UnicodeError:
        # not ascii
        encoded = raw.encode('utf-8')
        if version == 'cus' or version == 'cns':
          encoded = encoded.replace(' ', '')
          encoded = encoded.strip()
        outfile.write('%s\n' % encoded)
      else:
        # ascii
        outfile.write(raw + '\n')

  print 'Success! Goodbye.'
  outfile.close()

if __name__ == '__main__':
  main()