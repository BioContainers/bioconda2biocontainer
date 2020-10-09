#!/usr/bin/env python
import argparse

import yaml

from bioconda2biocontainer import __version__
from bioconda2biocontainer.update_cwl_docker_image import update_cwl_docker_from_tool_name


def main():
    parser = argparse.ArgumentParser(
        description='Replace Docker image in CWL from conda env yaml file')

    parser.add_argument('-v', '--version', action='version',
                        version='PM4NGS version: {}'.format(__version__))
    parser.add_argument('--conda_env_file', help='Conda env yaml file',
                        required=True)
    parser.add_argument('--cwl_path', help='Path to the CWL directory',
                        required=True)
    args = parser.parse_args()

    with open(args.conda_env_file) as fin:
        conda_env = yaml.load(fin, Loader=yaml.FullLoader)
        if 'dependencies' in conda_env:
            for d in conda_env['dependencies']:
                update_cwl_docker_from_tool_name(d, args.cwl_path)


if __name__ == '__main__':
    main()
