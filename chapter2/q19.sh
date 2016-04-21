#!/bin/bash

cut -f1 hightemp.txt | sort | uniq -c | sort -nk1 -r
