#!/usr/bin/env python3
# mcb.pyw - Saves and loads pieces of text to the clipboard
# Usage: ./mcb.pyw save <keyword> - Saves clipboard to keyword
#        ./mcb.pyw load <keyword> - Loads keyword content to clipboard
#        ./mcb.pyw list - Lists all keywords


import shelve
import pyperclip
import argparse


mcbShelf = shelve.open('mcb')

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest='command')

# Save to keyword
save = subparsers.add_parser('save',
                             help="Save clipboard content to keyword")
save.add_argument('keyword',
                  help='keyword to save data to')

# Load from keyword
load = subparsers.add_parser('load', help="Load content from keyword to\
                             clipboard")
load.add_argument('keyword',
                  help='keyword to load content to clipboard from')

# List keywords
list_content = subparsers.add_parser('list', help="List keywords.")

args = parser.parse_args()

if args.command == 'save':
    print('Saved content to <{0}>.'.format(args.keyword))
    mcbShelf[args.keyword] = pyperclip.paste()
elif args.command == 'load':
    if args.keyword in mcbShelf:
        print("""
                Added content for <{key}> to clipboard.\n
                Content:\n
                \t{content}
              """.format(key=args.keyword, content=mcbShelf[args.keyword]))
        pyperclip.copy(mcbShelf[args.keyword])
    else:
        print('Could not find keyword.')

elif args.command == 'list':
    print(str(list(mcbShelf.keys())))


mcbShelf.close()
