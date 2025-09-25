#!/usr/bin/env python
import argparse
import json

from bioconda2biocontainer import __version__
from bioconda2biocontainer.biocontainer import find_package_by_name, find_latest_image


def find_tool(package_name, print_json):
    tool = find_package_by_name(package_name)
    if isinstance(tool, dict):
        if print_json:
            print(json.dumps(tool, indent=4))
        else:
            print('id\tversion\turl')
            for v in tool['versions']:
                print('{}\t{}\t{}'.format(v['id'], v['meta_version'], v['url']))
    else:
        print('No package {} found'.format(package_name))


def find_latest_image_main(package_name, package_version, json, all, sort_by_size,
                           sort_by_download, container_type, registry_host):
    images = find_latest_image(package_name, package_version, all, sort_by_size,
                               sort_by_download, container_type, registry_host)
    if isinstance(images, list):
        if json:
            print(json.dumps(images, indent=4))
        elif all:
            print('image\tupdated\tsize\tdownloads\tcontainer_type')
            for i in images:
                image_name = '' if 'image_name' not in i else i['image_name']
                image_type = '' if 'image_type' not in i else i['image_type']
                updated = '' if 'updated' not in i else i['updated']
                size = '' if 'size' not in i else i['size']
                downloads = '' if 'downloads' not in i else i['downloads']
                print('{}\t{}\t{}\t{}\t{}'.format(
                    image_name, updated,
                    size, downloads,
                    image_type))
    elif isinstance(images, dict):
        print(images['image_name'])
    else:
        if container_type:
            print('No version {} available for package {} with container type {}'.format(
                package_version, package_name, container_type))
        else:
            print('No version {} available for package {}'.format(package_version, package_name))
        print('Searching available versions for package {}'.format(package_name))
        find_tool(package_name, False)


def main():
    parser = argparse.ArgumentParser(
        description='Find Biocontainers images from Bioconda packages')

    parser.add_argument('-v', '--version', action='version',
                        version='PM4NGS version: {}'.format(__version__))
    parser.add_argument('--package_name', help='Bioconda package name',
                        required=True)
    parser.add_argument('--package_version', help='Bioconda package version',
                        required=False)
    parser.add_argument('--container_type', help='Container type. Default: Docker. '
                                                 'Values: Docker, Conda, Singularity',
                        default=None, required=False)
    parser.add_argument('--registry_host', help='Registry host. Default: quay.io.'
                                                'Values: ',
                        default=None, required=False)
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
                               args.sort_by_size, args.sort_by_download,
                               args.container_type, args.registry_host)
    else:
        find_tool(package_name, args.json)


if __name__ == '__main__':
    main()
