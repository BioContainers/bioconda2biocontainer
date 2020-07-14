import json

import requests

base_url = "http://api.biocontainers.pro/ga4gh/trs/v2/tools"


def request_url_to_dict(url):
    response = requests.get('{}'.format(url))
    if response.status_code == 200:
        return json.loads(response.text)
    return response.status_code


def find_package_by_name(package_name):
    data = request_url_to_dict('{0}/{1}'.format(base_url, package_name))
    if type(data) == int:
        return data
    if data and 'versions' in data:
        versions = data['versions']
        data['versions'] = sorted(versions, key=lambda i: i['meta_version'], reverse=True)
    return data


def find_package_by_term(search_term):
    data = request_url_to_dict('{0}?all_fields_search={1}'.format(base_url, search_term))
    return data


def filter_by_container_registry(container_type, registry_host, i):
    if registry_host and container_type and \
            i['registry_host'].startswith(registry_host) and \
            container_type == i['image_type']:
        return True
    if not registry_host and container_type and \
            container_type == i['image_type']:
        return True
    if registry_host and not container_type and \
            i['registry_host'].startswith(registry_host):
        return True
    if not registry_host and not container_type:
        return True
    return False


def find_latest_image(package_name, package_version, all, sort_by_size,
                      sort_by_download, container_type, registry_host):
    data = request_url_to_dict('{0}/{1}/versions/{1}-{2}'.format(
        base_url, package_name, package_version))
    if type(data) == dict or type(data) == list:
        versions = []
        if data and 'images' in data:
            for i in data['images']:
                if filter_by_container_registry(container_type, registry_host, i):
                    if 'downloads' not in i:
                        i['downloads'] = 0
                    versions.append(i)
        if sort_by_size:
            versions = sorted(versions, key=lambda i: i['size'])
        elif sort_by_download:
            versions = sorted(versions, key=lambda i: i['downloads'], reverse=True)
        else:
            versions = sorted(versions, key=lambda i: i['updated'], reverse=True)
        if all:
            return versions
        return versions[0]
    return data
