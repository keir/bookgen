import csv
import sys

# The Sci-Fi book metadata CSV file from Shelfie has the following columns:
FIELDS = [
    'author',
    'title',
    'isbn',
    'publication_date',
    'publisher',
    'genre'
]

if len(sys.argv) != 2:
  sys.stdout.write('ERROR: missing metadata csv file argument')
  sys.exit(1)

# Format the output book title and author so that the neural network will learn
# to output the generated books in a machine-parsable format.
with open(sys.argv[1]) as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=FIELDS)
    for row in reader:
        print row['author'], '|||', row['title']
