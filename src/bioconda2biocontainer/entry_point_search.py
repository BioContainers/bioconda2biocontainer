#!/usr/bin/env python
import argparse
import json

from bioconda2biocontainer import __version__
from bioconda2biocontainer.biocontainer import find_package_by_term


def print_tools_table(data):
    print('name\tversions\tdescription\tlicense\tpulls')
    for d in data:
        print('{}'.format(d['name']), end='\t')
        versions = sorted(d['versions'], key=lambda i: i['meta_version'], reverse=True)
        print(','.join(map(lambda x: x['meta_version'], versions)), end='\t')
        if 'license' not in d:
            d['license'] = 'Not available'
        print('{}\t{}\t{}'.format(d['description'].replace('\n', ''), d['license'], d['pulls']))


def main():
    parser = argparse.ArgumentParser(
        description='Find Biocontainers tools')

    parser.add_argument('-v', '--version', action='version',
                        version='PM4NGS version: {}'.format(__version__))
    parser.add_argument('--search_term', help='Search term',
                        required=True)
    parser.add_argument('--json', help='Print json format', action='store_true',
                        required=False)
    parser.add_argument('--show_images', help='Show all available images',
                        action='store_true', required=False)
    args = parser.parse_args()
    search_term = args.search_term

    data = find_package_by_term(search_term)
    if isinstance(data, int):
        print('No packages found with search term: {}'.format(search_term))
    elif args.json:
        print(json.dumps(data, indent=4))
    else:
        print_tools_table(data)


if __name__ == '__main__':
    main()
