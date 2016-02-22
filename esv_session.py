# ESVSession class

import urllib

class ESVSession:
    def __init__(self, key):
        options = ['include-short-copyright=0',
                   'output-format=plain-text',
                   'include-passage-horizontal-lines=0',
                   'include-heading-horizontal-lines=0',
                   'include-passage-references=false',
                   'include-first-verse-numbers=false',
                   'include-verse-numbers=false',
                   'include-footnotes=false',
                   'include-short-copyright=false',
                   'include-headings=false',
                   'include-subheadings=false',
                   'include-selahs=false',
                   'include-content-type=false',
                   'line-length=0']
        self.options = '&'.join(options)
        self.baseUrl = 'http://www.esvapi.org/v2/rest/passageQuery?key=%s' % (key)

    def doPassageQuery(self, passage):
        passage = passage.split()
        passage = '+'.join(passage)
        url = self.baseUrl + '&passage=%s&%s' % (passage, self.options)
        page = urllib.urlopen(url)
        return page.read()