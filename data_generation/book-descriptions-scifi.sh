#!/bin/bash

th train.lua \
-gpuid 0 \
-eval_val_every 500 \
-data_dir data/book-descriptions-scifi \
-rnn_size 400 \
-num_layers 3 \
-dropout 0.3 \
-seq_length 50 \
-batch_size 25 \
-savefile book-descriptions-scifi 
