#!/bin/bash

th sample.lua \
-gpuid 0 \
-temperature 1 \
-primetext "$1" \
$2
