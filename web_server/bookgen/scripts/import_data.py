import setup_django
from generation.models import *

file = open('romance-titles-generated.txt','r')
file2 = open('mix-scifi-romance-60-40-authors-generated.txt','r')

lines = file.readlines()
lines2 = file2.readlines()

for line1, line2 in zip(lines,lines2):
    if line1 and line2:
        try:
            b = Book.objects.create(title=line1.strip(), author=line2.strip(), genre="romance")
            print line1.strip()
        except:
            continue