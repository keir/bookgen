#!/bin/bash

if [ ! -e make_data.sh ] ; then
  echo 'ERRO: Must be in same directory as make_data.sh'
  exit 1
fi

# Sci-fi
python munge_book_data_for_rnn.py ../../book_metadata.csv > ../book_titles_and_author_scifi.txt
python munge_book_descriptions_for_rnn.py ../../book_metadata_summary.csv > ../book_descriptions_scifi.txt

rm -f ../../../ManRNN/char-rnn/data/book-titles-and-author-scifi/*.t7
cp ../book_titles_and_author_scifi.txt ../../../ManRNN/char-rnn/data/book-titles-and-author-scifi/input.txt

rm -f ../../../ManRNN/char-rnn/data/book-descriptions-scifi/*.t7
cp ../book_descriptions_scifi.txt ../../../ManRNN/char-rnn/data/book-descriptions-scifi/input.txt

# Self-help
python munge_book_data_for_rnn.py ../../self_help.csv > ../book_titles_and_author_selfhelp.txt
python munge_book_descriptions_for_rnn.py ../../self_help_summary.csv > ../book_descriptions_selfhelp.txt

rm -f ../../../ManRNN/char-rnn/data/book-titles-and-author-selfhelp/*.t7
cp ../book_titles_and_author_selfhelp.txt ../../../ManRNN/char-rnn/data/book-titles-and-author-selfhelp/input.txt

rm -f ../../../ManRNN/char-rnn/data/book-descriptions-selfhelp/*.t7
cp ../book_descriptions_selfhelp.txt ../../../ManRNN/char-rnn/data/book-descriptions-selfhelp/input.txt
