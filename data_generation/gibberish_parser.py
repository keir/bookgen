import sys

"""
>>> Author H. Name ### The Book Title |||
A riveting description of the book goes here.  Buct ceare, imet theytore
beturpel cith in a Mazing meen to fifen Batabe auses. Icter is erigy to bcing
scomicangus, rovulo, mear relige, Tompanges Sua on Jhact Kome-sevoring and
muriuled with castess. Imaliol to a promic and arout at exwels her. Thers the
unierater. Have head Cimstspent, the is gatre timishing asder as AnortTaterlage
of Mechative, and fatf-- chrunieg contry toree. In the one a wrelura wistor and
Tinstede wakan rereass chowed wolknos. The exdiis

>>> Writer B. Nick ### Another Book Title |||
A riveting description of the book goes here.  Buct ceare, imet theytore
beturpel cith in a Mazing meen to fifen Batabe auses. Icter is erigy to bcing
"""

import re
title_author_pattern = re.compile('^>>> (.+) ### (.+) |||$')

num_total = 0
num_invalid_split = 0
num_invalid_match = 0
num_junk = 0

all_gibberish_books = open(sys.argv[1]).read()
for maybe_gibberish_book in all_gibberish_books.split('\n\n'):
  print '.',
  maybe_gibberish_book = maybe_gibberish_book.strip()

  # Each book sholud be just 2 lines: title/author and description.
  try:
    title_and_author, description = maybe_gibberish_book.split('\n')
  except ValueError:
    num_invalid_split += 1
    continue

  # Get title and author.
  match = title_author_pattern.match(title_and_author)
  if not match:
    num_invalid_match += 1
    continue
  title, author = match.groups()

  # Look for junk inside the description.
  if any((junk in description) for junk in ('|||', '>>>', '###')):
    num_junk += 1
    continue

  print repr([title, author, description])

sys.stderr.write('Total: %d, invalid split: %d, invalid match: %d, junk: %d\n' %
                 (num_total, num_invalid_split, num_invalid_match, num_junk))

