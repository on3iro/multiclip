#!/usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: ./mcb.pyw save <keyword> - Saves clipboard to keyword
#        ./mcb.pyw <keyword> - Loads keyword to clipboard
#        ./mcb.pyw list - Loads all keywords to clipboard


import shelve
import pyperclip
import argparse
import sys


mcbShelf = shelve.open('mcb')

parser = argparse.ArgumentParser()
parser.add_argument('save',
                    nargs=2,
                    help="Saves clipboard to keyword")
args = parser.parse_args()
print(args)

# TODO: Save clipboard content
#  if len(sys.argv) == 3 and sys.argv[1].lower() == 'save':
    #  mcbShelf[sys.argv[2]] = pyperclip.paste()
#  elif len(sys.argv) == 2:
    # TODO: List keywords and load content


mcbShelf.close()
