# -*- coding: utf-8 -*-
__author__ = 'wogong'

import argparse
import csv
import os
import sys
import datetime

doc = """
    This is a simple script created by wogong, 
    that converts Weread notes export to a csv compatible with Readwise.

    Steps:
        1. In Weread, go into your notes, click "export/导出"
        2. Click "Copy to clipboard/复制到剪贴板”
        3. Paste the copied notes into a txt file.
        4. Run this script by typing 'weread2readwise.py --path [txt file path]', the script will create a csv file
        5. In Readwise, import the csv file in this page: https://readwise.io/import_bulk
"""
parser = argparse.ArgumentParser(description=doc, formatter_class=argparse.RawTextHelpFormatter)
parser.add_argument("--path", help="The path of input Weread note txt file")
parser.add_argument("--url", default='', help="The url of the import book")
parser.add_argument("--date", default='', help="The date you want to specify instead of now, format YYYY-MM-DD")

args = parser.parse_args()
path = args.path
if not os.path.isfile(path):
    print('The path specified does not exist, make sure it is a txt file')
    sys.exit()
URL = args.url
LOCATION = ""
DATE = args.date if args.date else datetime.datetime.now().strftime('%Y-%m-%d')


with open(path, 'r') as weread:
    title = weread.readline().strip('\n')
    author = weread.readline().strip('\n')
    lines = weread.readlines()

notes = []
note = ""
for i,line in enumerate(lines):
    line = line.strip('\n')
    # chapter beginning, format '◆ chapter title'
    if line.startswith('◆'):
        chapter = line.strip('◆ ')
    # underlined highlight without note
    elif line.startswith('>>'):
        highlight = line.strip('>> ') + '  ——  ' + chapter
        notes.append([highlight, title, author, URL, note, LOCATION, DATE])
        note = ""
    elif line != '':
        if 'chapter' in dir():
            note = line
        else:
            print('line {} not processed. content: {}'.format(i,line))

# write to csv
with open(path[:path.index('txt')] + 'csv', 'w', newline='') as readwise:
    writer = csv.writer(readwise)
    # initialize headers
    writer.writerow(['Highlight', 'Title', 'Author', 'URL', 'Note', 'Location', 'Date'])
    writer.writerows(notes)