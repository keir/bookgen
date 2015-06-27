import csv

# The Sci-Fi book metadata CSV file from Shelfie has the following columns:
FIELDS = [
    'author',
    'title',
    'isbn',
    'publication_date',
    'publisher',
    'genre'
]

with open('../book_metadata.csv') as csvfile:
    reader = csv.DictReader(csvfile, fieldnames=FIELDS)
    for row in reader:
        print row['author'], '|||', row['title']
