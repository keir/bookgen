from django.shortcuts import render
from django.http import HttpResponse
import random
import requests
import urllib2
import xml.etree.ElementTree as ET

from generation.models import *

FLICKR_KEY = '4af6e51eed0bc2c6edde393cd84a699d'
IMG_URL = 'https://farm%s.staticflickr.com/%s/%s_%s_%s.jpg'

def get_base_image(genre):
    
    url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=%s&text=%s&licenses=2,4&content_type=1" % (FLICKR_KEY, genre)
    
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
            


def get_image(title, genre):
    
    url = "https://api.flickr.com/services/rest/?method=flickr.photos.search&api_key=%s&text=%s&licenses=2,4&content_type=1" % (FLICKR_KEY, title + " " + genre)
    
    try:
        usock = urllib2.urlopen(url) 
        txt = usock.read()
    except:
        return None
    
    try:
        tree = ET.fromstring(txt)
    except:
        return get_base_image(genre)
    
    imgs = []
    count = 0
    
    for photos in tree.findall('photos'):
        for photo in photos.findall('photo'):
            count += 1
            imgs.append(IMG_URL % (photo.attrib['farm'], photo.attrib['server'], photo.attrib['id'], photo.attrib['secret'], 'z'))

    if count == 0:
        return get_base_image(genre)
    r = random.randint(0, count -1)
    return imgs[r]
            
def home(request):
    genre = request.GET.get('genre')
    if genre:
        book = Book.objects.filter(genre=genre).order_by('?').first()
    else:  
        book = Book.objects.order_by('?').first()
        genre = book.genre
        
    if genre == 'mix':
        font = Font.objects.order_by('?').first().name
        colors = ColorPalette.objects.order_by('?').first()
    else:
        font = Font.objects.filter(genre=genre).order_by('?').first().name
        colors = ColorPalette.objects.filter(genre=genre).order_by('?').first()
    
    url = get_image(book.title, genre)
    
    return render(request, 'generation/home.html', {'book': book, 'font': font, 'image_url': url, 'colors': colors, 'genre': genre})


def proxy_image(request):
    print 'Got proxy call!!!'
    try:
        image_data = requests.get(request.GET['theurl']).content
        print 'Fetched:', request.GET['theurl']
    except Exception as ex:
        print 'Got exception:', ex
        return
    return HttpResponse(image_data, content_type='image/jpg')
