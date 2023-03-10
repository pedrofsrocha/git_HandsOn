#!/usr/bin/env python

import sys, re
from argparse import ArgumentParser

parser = ArgumentParser(description = 'Classify a sequence as DNA or RNA')
parser.add_argument("-s", "--seq", type = str, required = True, help = "Input sequence")
#Identify motifs
parser.add_argument("-m", "--motif", type = str, required = False, help = "Motif")

if len(sys.argv) == 1:
    parser.print_help()
    sys.exit(1)

args = parser.parse_args()

args.seq = args.seq.upper()
if re.search('^[ACGTU]+$', args.seq):
    if re.search('T', args.seq) and not ('U', args.seq):
        print ('The sequence is DNA')
    elif re.search('U', args.seq) and not ('T', args.seq): # addding the  option 
of sequences that contain T and U.
        print ('The sequence is RNA')
    else:
        print ('The sequence is not DNA or RNA')
else:
    print ('The sequence can be DNA nor RNA')

if args.motif:
    args.motif = args.motif.upper()
    print(f'Motif search enabled: looking for motif "{args.motif}" in sequence "{args.seq}"... ', end = '')
    if re.search(args.motif, args.seq):
        print("Just find it")
    else:
        print("NO MOTIF FOUND")
