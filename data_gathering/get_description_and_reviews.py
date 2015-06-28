
import urllib2
import xml.etree.ElementTree as ET
import sqlite3

GOODREADS_KEY = 'tS4AZr3qhInGYME1VeuQGg'


def get_goodreads(isbn):
    url = 'https://www.goodreads.com/book/isbn?format=xml&isbn=%s&key=%s&user_id=29299648' % (isbn, GOODREADS_KEY)
    
    try:
        usock = urllib2.urlopen(url) 
        txt = usock.read()
    except:
        return None
    
    tree = ET.fromstring(txt)
    
    for book in tree.findall('book'):
        desc = book.find('description')
        print desc.text
        return desc.text
        
import csv

book_info = {}
file2 = open('book_metadata_summary.csv','a')

ok = False

with open('book_metadata.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    for vals in reader:
        author = vals[0]
        title = vals[1]
        isbn = vals[2]
        if isbn == '9781439132876':
            ok = True
        if ok:
            desc = get_goodreads(isbn)
        
            res = '%s,%s,%s,"%s"' % (isbn, author, title, desc)
        
            file2.write(res + '\n')
