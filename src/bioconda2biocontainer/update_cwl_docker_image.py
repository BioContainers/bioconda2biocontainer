import os

import yaml

from bioconda2biocontainer.biocontainer import find_latest_image

PRINT_HEADER = True


def __replace_docker_image(f, old, new, package_name, package_version):
    global PRINT_HEADER
    if PRINT_HEADER:
        print('{} with version {} update image to: {}'.format(
            package_name, package_version,
            new))
        PRINT_HEADER = False
    print('\t{} with old image replaced: {}'.format(f, old))
    with open(f) as fin:
        list_of_lines = fin.readlines()
    with open(f, 'w') as fout:
        for line in list_of_lines:
            if old in line:
                line = line.replace(old, new)
            fout.write(line)


def __load_cwl(f, package_name, package_version, image_name):
    with open(f) as fin:
        try:
            y = yaml.load(fin, Loader=yaml.FullLoader)
            return y
        except yaml.scanner.ScannerError:
            pass
    return None


def __replace_in_cwl(f, package_name, package_version, image_name):
    y = __load_cwl(f, package_name, package_version, image_name)
    if y:
        if 'hints' in y and 'DockerRequirement' in y['hints'] and \
                'dockerPull' in y['hints']['DockerRequirement'] and \
                y['hints']['DockerRequirement']['dockerPull'].split(':')[0] == \
                image_name.split(':')[0] and \
                y['hints']['DockerRequirement']['dockerPull'] != image_name:
            __replace_docker_image(f,
                                   y['hints']['DockerRequirement']['dockerPull'], image_name,
                                   package_name, package_version)


def __replace_in_yml(f, package_name, package_version, image_name):
    y = __load_cwl(f, package_name, package_version, image_name)
    if y:
        if 'dockerPull' in y and y['dockerPull'].split(':')[0] == image_name.split(':')[0] and \
                y['dockerPull'] != image_name:
            __replace_docker_image(f,
                                   y['dockerPull'], image_name,
                                   package_name, package_version)


def update_cwl_docker_from_biocontainers(package_name, package_version, cwl_path):
    biocontainer_image = find_latest_image(package_name, package_version, False,
                                           False, False, 'Docker', None)
    if isinstance(biocontainer_image, dict):
        for root, dirs, files in os.walk(cwl_path):
            for f in files:
                f = os.path.join(root, f)
                if f.endswith('.cwl'):
                    __replace_in_cwl(f, package_name, package_version,
                                     biocontainer_image['image_name'])
                elif f.endswith('.yml') or f.endswith('.yaml'):
                    __replace_in_yml(f, package_name, package_version,
                                     biocontainer_image['image_name'])
    else:
        print('There is not biocontainer image for {} version {}'.format(
            package_name, package_version))


def update_cwl_docker_from_tool_name(tool, cwl_path):
    global PRINT_HEADER
    PRINT_HEADER = True
    if isinstance(tool, str) and '=' in tool:
        tool_version = tool.split('=')
        update_cwl_docker_from_biocontainers(
            tool_version[0], tool_version[1], cwl_path)
