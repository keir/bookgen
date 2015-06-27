import csv
import sys

import unicodedata

def strip_unicode(value):
  return unicodedata.normalize(
          'NFKD',
          unicode(value, 'utf-8')
      ).encode('ascii', 'ignore')

def strip_tags(text):
  return (text.replace('<br>', '')
              .replace('<em>', '')
              .replace('</em>', '')
              .replace('<strong>', '')
              .replace('</strong>', '')
         )

def clean(text):
  if text and text != 'None':
    return strip_tags(strip_unicode(text)).strip()
  return ''

# The Sci-Fi book metadata CSV file from Amy's scraper has the following format.
FIELDS = [
    'isbn',
    'author',
    'title',
    'description'
]

if len(sys.argv) != 2:
    sys.stdout.write('ERROR: missing metadata csv file argument')
    sys.exit(1)

# Format the output book title and author so that the neural network will learn
# to output the generated books in a machine-parsable format.
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=FIELDS)
    for row in reader:
        description = clean(row['description'])
        author = clean(row['author'])
        title = clean(row['title'])
        if description:
          print '>>>', title, '###', author, '|||'
          print description
          print
