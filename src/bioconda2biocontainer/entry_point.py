#!/usr/bin/env python
import argparse
import json

from bioconda2biocontainer.biocontainer import find_package_by_name, find_latest_image


def find_tool(package_name, print_json):
    tool = find_package_by_name(package_name)
    if type(tool) == dict:
        if print_json:
            print(json.dumps(tool, indent=4))
        else:
            print('id\tversion\turl')
            for v in tool['versions']:
                print('{}\t{}\t{}'.format(v['id'], v['meta_version'], v['url']))
    else:
        print('No package {} found'.format(package_name))


def find_latest_image_main(package_name, package_version, json, all, sort_by_size,
                           sort_by_download, registry_host):
    images = find_latest_image(package_name, package_version, all, sort_by_size,
                               sort_by_download, registry_host)
    if type(images) == list:
        if json:
            print(json.dumps(images, indent=4))
        elif all:
            print('image\tupdated\tsize\tdownloads')
            for i in images:
                print('{}\t{}\t{}\t{}'.format(
                    i['image_name'], i['updated'], i['size'], i['downloads']))
    elif type(images) == dict:
        print(images['image_name'])
    else:
        print('No version {} available for package {}'.format(package_version, package_name))
        print('Searching available versions for package {}'.format(package_name))
        find_tool(package_name, False)


def main():
    parser = argparse.ArgumentParser(
        description='Find Biocontainers images from Bioconda packages')

    parser.add_argument('--package_name', help='Bioconda package name',
                        required=True)
    parser.add_argument('--package_version', help='Bioconda package version',
                        required=False)
    parser.add_argument('--registry_host', help='Registry host. Default: quay.io',
                        default='quay.io', required=False)
    parser.add_argument('--json', help='Print json format', action='store_true',
                        required=False)
    parser.add_argument('--all', help='Print all images', action='store_true',
                        required=False)
    parser.add_argument('--sort_by_size', help='Sort by size instead of by date',
                        action='store_true', required=False)
    parser.add_argument('--sort_by_download',
                        help='Sort by number of downloads instead of by date',
                        action='store_true', required=False)
    args = parser.parse_args()
    package_name = args.package_name
    package_version = None
    if args.package_version:
        package_version = args.package_version

    if package_version:
        find_latest_image_main(package_name, package_version, args.json, args.all,
                               args.sort_by_size, args.sort_by_download, args.registry_host)
    else:
        find_tool(package_name, args.json)


if __name__ == '__main__':
    main()
