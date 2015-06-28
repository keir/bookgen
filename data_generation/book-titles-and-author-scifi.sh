#!/bin/bash

th train.lua \
-gpuid 0 \
-eval_val_every 500 \
-data_dir data/book-titles-and-author-scifi \
-rnn_size 300 \
-num_layers 3 \
-dropout 0.3 \
-seq_length 50 \
-batch_size 25 \
-savefile book-titles-and-author-scifi
