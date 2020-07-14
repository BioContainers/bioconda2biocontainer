import json

import requests

base_url = "http://api.biocontainers.pro/ga4gh/trs/v2/tools"


def find_package_by_name(package_name):
    response = requests.get('{0}/{1}'.format(base_url, package_name))
    if response.status_code == 200:
        data = json.loads(response.text)
        if data and 'versions' in data:
            versions = data['versions']
            data['versions'] = sorted(versions, key=lambda i: i['meta_version'], reverse=True)
        return data
    return response.status_code


def find_latest_image(package_name, package_version, all, sort_by_size,
                      sort_by_download, registry_host='quay.io'):
    response = requests.get('{0}/{1}/versions/{1}-{2}'.format(
        base_url, package_name, package_version))
    if response.status_code == 200:
        data = json.loads(response.text)
        versions = []
        if data and 'images' in data:
            for i in data['images']:
                if i['registry_host'].startswith(registry_host):
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
    return response.status_code
