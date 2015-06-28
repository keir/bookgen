from django.shortcuts import render
import random
import urllib2
import xml.etree.ElementTree as ET

from generation.models import *

FLICKR_KEY = '4af6e51eed0bc2c6edde393cd84a699d'
IMG_URL = 'https://farm%s.staticflickr.com/%s/%s_%s_%s.jpg'

def get_image(title, genre):
    
    url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=%s&text=%s&licenses=2,4&content_type=1" % (FLICKR_KEY, title + " " + genre)
    
    try:
        usock = urllib2.urlopen(url) 
        txt = usock.read()
    except:
        return None
    
    tree = ET.fromstring(txt)
    
    imgs = []
    count = 0
    
    for photos in tree.findall('photos'):
        for photo in photos.findall('photo'):
            count += 1
            imgs.append(IMG_URL % (photo.attrib['farm'], photo.attrib['server'], photo.attrib['id'], photo.attrib['secret'], 'z'))
            
    r = random.randint(0, count -1)
    return imgs[r]
            
def home(request):
    
    book = Book.objects.order_by('?').first()
    genre = book.genre
    
    font = Font.objects.filter(genre=genre).order_by('?').first().name
    
    url = get_image(book.title, genre)
    
    return render(request, 'generation/home.html', {'book': book, 'font': font, 'image_url': url})