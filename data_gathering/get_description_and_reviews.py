
import urllib2
import xml.etree.ElementTree as ET
import sqlite3
from BeautifulSoup import BeautifulSoup
import re

GOODREADS_KEY = 'tS4AZr3qhInGYME1VeuQGg'


def get_goodreads(isbn):
    url = 'https://www.goodreads.com/book/isbn?format=xml&isbn=%s&key=%s&user_id=29299648' % (isbn, GOODREADS_KEY)
    
    try:
        usock = urllib2.urlopen(url) 
        txt = usock.read()
    except:
        return None
    
    tree = ET.fromstring(txt)
    
    reviews = []
    
    for book in tree.findall('book'):
        #desc = book.find('description')
        #print desc.text
        #return desc.text
        review = book.find('reviews_widget')
        val = review.text.split('<iframe id="the_iframe" src="')
        val2 = val[1].split('" width="565" height="400" frameborder="0">')
        url2 = val2[0]
        
        try:
            usock2 = urllib2.urlopen(url2) 
            txt2 = usock2.read()
        except:
            return None
        bs = BeautifulSoup(txt2)
        for item in bs.findAll('div',{'class':'gr_review_container'}):
            bs_val = re.sub('<[^<]+?>', '  ', str(item))
            bs_val = re.sub('&middot;', '  ', bs_val)
            bs_val = re.sub("\s+"," ", bs_val)
            reviews.append(bs_val)
    return reviews

import csv

book_info = {}
file2 = open('self_help_reviews.csv','a')

ok = False

with open('self_help.csv','rb') as csvfile:
    reader = csv.reader(csvfile)
    for vals in reader:
        author = vals[0]
        title = vals[1]
        isbn = vals[2]
        reviews = get_goodreads(isbn)
    
        if reviews:
            for review in reviews:
                res = '%s,%s,%s,"%s"' % (isbn, author, title, review)
        
                file2.write(res + '\n')
