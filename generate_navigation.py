#!/usr/bin/env python3

import argparse
import re
import os
import sys
import string
import yaml  # depends on PyYAML
from collections import OrderedDict


# Categories
# Dict containing category name (keys) and short name used for url
categories = OrderedDict()
categories['Author Instructions'] = 'authors'
categories['Editorial Policies'] = 'policies'
categories['About LiveCoMS'] = 'about'


def get_category_folder(category):
    return '_' + category.lower().replace(' ', '_')


def get_permalink(filename, category):
    return categories[category] + '/' + os.path.basename(filename).replace('.md', '')[3:] + '/'


def make_link_from_heading(heading):
    translator = str.maketrans('', '', string.punctuation)
    translator.pop(45)  # don't replace '-'
    return heading.translate(translator).lower().replace(' ', '-')


def print_subtoc(headings, level, file_location):
    for h in headings:
        # We'll put the title between quotation marks to allow for colons,
        # so we need to escape any quotation marks in the title
        title = h['title'].replace('"', '\\"')
        print(level*2*' ' + '- title: "' + title + '"')
        print(level*2*' ' + '  url: ' + file_location + h['ref'])
        if h['sub']:
            print(level*2*' ' + '  children:')
            print_subtoc(h['sub'], level + 1, file_location)


def create_toc(md_file, category):
    find_heading = re.compile('^(#+) (.*)')
    headings = []

    file_contents = open(os.path.join(get_category_folder(category), md_file)).read().split('\n')

    header = []
    if file_contents[0] == '---':
        n = 0
        for n, line in enumerate(file_contents[1:]):
            if line == '---':
                n += 1
                break
        header = file_contents[1:n]
        file_contents = file_contents[n+1:]

    # Process front matter
    title = ''

    header_string = '\n'.join(header)

    front_matter = yaml.load(header_string)

    rewrite_frontmatter = False

    if 'title' in front_matter:
        title = front_matter['title']

    if 'permalink' in front_matter:
        permalink = front_matter['permalink']
    else:
        permalink = get_permalink(md_file.name, category)
        header.append('permalink: ' + permalink)
        rewrite_frontmatter = True
    permalink += 'index.html'

    if 'sidebar' not in front_matter or 'nav' not in front_matter['sidebar']:
        nav = categories[category] + '_' + os.path.basename(md_file.name)[3:-3]
        header.append('sidebar:')
        header.append('  nav: ' + nav)
        rewrite_frontmatter = True
    else:
        nav = front_matter['sidebar']['nav']

    if rewrite_frontmatter:
        with open(os.path.join(get_category_folder(category), md_file)) as f:
            f.write('---\n')
            for line in header:
                f.write(line + '\n')
            f.write('---\n')
            for line in file_contents:
                f.write(line + '\n')

    headings.append({'title': title,
                     'ref': '#',
                     'sub': []})

    # Read remaining file
    for line in file_contents:
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
        
    print(nav + ':')
    print_subtoc(headings, 1, permalink)


def main(args):
    # argparse might be overkill, but at least we have a little help file
    parser = argparse.ArgumentParser(description=('Generate YAML table of content ' +
                                                  'from markdown files located in category-folders' +
                                                  '(hardcoded at the top of this script)\n' +
                                                  'Output of this script should be redirected to ' +
                                                  '_data/navigation.yml'),
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.parse_args(args)

    # print main navigation
    print('main:')
    for c in categories:
        print('  - title: ' + c)
        print('    url: /' + categories[c] + '/')

    # print sidebar navigation for files
    for c in categories:
        for f in os.listdir(get_category_folder(c)):
            if f.endswith('.md') and f != 'index.md':
                print()
                create_toc(f, c)


if __name__ == "__main__":
    main(sys.argv[1:])
