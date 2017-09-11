#!/usr/bin/env python3

import argparse
import re
import os
import string


# List of Markdown files that will 
#   - be referred to in the list of links on the top of the page
#   - have a sidebar navigation item
markdown_files = [
    {'title': 'Policies', 'file': 'policies.md'},
    {'title': 'Best Practices', 'file': 'best_practices.md'},
    {'title': 'Reviews', 'file': 'perpetual_reviews.md'},
    {'title': 'Simulation Comparisons', 'file': 'compare_simulations.md'},
    {'title': 'Tutorials', 'file': 'tutorials.md'},
    {'title': 'Lessons Learned', 'file': 'lessons_learned.md'},
    {'title': 'Paper Writing', 'file': 'paper_code.md'},
    {'title': 'Editorial Board', 'file': 'editorial_board.md'} ]

def print_subtoc(headings, level, file_location):
    for h in headings:
        print(level*2*' ' + '- title: ' + h['title'])
        print(level*2*' ' + '  url: ' + file_location + h['ref'])
        if h['sub']:
            print(level*2*' ' + '  children:')
            print_subtoc(h['sub'], level + 1, file_location)

def get_folder_from_filename(filename):
    if filename == 'index.md':
        return '/'
    else:
        return '/' +  filename.replace('.md', '') + '/'

def make_link_from_heading(heading):
    translator = str.maketrans('', '', string.punctuation)
    return heading.translate(translator).lower().replace(' ','-')

def create_toc(md_file):
    file_location = get_folder_from_filename(md_file.name) + 'index.html'
    find_heading = re.compile('^(#+) (.*)')
    headings = []

    # Process front matter
    title = ''
    line = md_file.readline()
    if line == '---\n':
        line = md_file.readline()
        while line != '---\n':
            line = [l.strip() for l in line.split(':', maxsplit=1)]
            if line and line[0] == 'title' and len(line) == 2:
                title = line[1]
            line = md_file.readline()
    else:
        md_file.seek(0)

    headings.append({'title': title,
                     'ref': '#',
                     'sub': []})

    # Read remaining file
    for line in md_file:
        match = find_heading.match(line)
        if match is None:
            continue
        heading_level = len(match.group(1))
        heading = match.group(2).strip()
        heading_ref = '#' + make_link_from_heading(heading)
        if heading_level == 1:
            headings.append({'title': heading,
                             'ref': heading_ref,
                             'sub': []})
        else:
            parent = headings
            for n in range(heading_level - 1):
                if len(parent) == 0:
                    parent.append({'title': '',
                                   'ref': '#',
                                   'sub': []})
                parent = parent[-1]['sub']
            parent.append({'title': heading,
                           'ref': heading_ref,
                           'sub': []})
        
    print(os.path.basename(md_file.name) + ':')
    print_subtoc(headings, 1, file_location)

# argparse might be overkill, but at least we have a little help file
parser = argparse.ArgumentParser(description=('Generate YAML table of content ' +
                                              'from markdown files ' +
                                              '(hardcoded at the top of this script)\n' +
                                              'Output of this script should be redirected to ' +
                                              '_data/navigation.yml'),
                                 formatter_class=argparse.RawTextHelpFormatter)

args = parser.parse_args()

# print main navigation
print('main:')
for f in markdown_files:
    print('  - title: ' + f['title'])
    print('    url: ' + get_folder_from_filename(f['file']))

# print sidebar navigation for files
for f in markdown_files:
    print()
    create_toc(open(f['file']))
