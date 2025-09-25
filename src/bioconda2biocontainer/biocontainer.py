import json
from typing import Optional, Union
import requests

base_url = "http://api.biocontainers.pro/ga4gh/trs/v2/tools"


def request_url_to_dict(url):
    response = requests.get('{}'.format(url))
    if response.status_code == 200:
        return json.loads(response.text)
    return response.status_code


def find_package_by_name(package_name):
    data = request_url_to_dict('{0}/{1}'.format(base_url, package_name))
    if isinstance(data, int):
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
            'image_type' in i and \
            container_type == i['image_type']:
        return True
    if registry_host and not container_type and \
            i['registry_host'].startswith(registry_host):
        return True
    if not registry_host and not container_type:
        return True
    return False


def _normalize_image_fields(image: dict) -> dict:
    """Ensure required fields exist in the image dict."""
    image.setdefault("downloads", 0)
    image.setdefault("updated", "")
    image.setdefault("size", 0)
    return image


def _sort_images(images: list[dict], sort_by_size: bool, sort_by_download: bool) -> list[dict]:
    """Sort images based on size, downloads, or updated date."""
    if sort_by_size:
        return sorted(images, key=lambda i: i["size"])
    if sort_by_download:
        return sorted(images, key=lambda i: i["downloads"], reverse=True)
    return sorted(images, key=lambda i: i["updated"], reverse=True)


def find_latest_image(
        package_name: str,
        package_version: str,
        all: bool = False,
        sort_by_size: bool = False,
        sort_by_download: bool = False,
        container_type: Optional[str] = None,
        registry_host: Optional[str] = None,
) -> Union[dict, list[dict], int, None]:
    """
    Retrieve the latest container image for a given package version.

    Args:
        package_name: Bioconda package name.
        package_version: Specific version string.
        all: If True, return all matching images instead of only the latest.
        sort_by_size: Sort by image size ascending.
        sort_by_download: Sort by download count descending.
        container_type: Optional filter by container type (e.g., 'Docker').
        registry_host: Optional filter by registry host.

    Returns:
        The latest image dict, a list of image dicts if all=True,
        an HTTP status code (int) on error, or None if no images found.
    """
    url = f"{base_url}/{package_name}/versions/{package_name}-{package_version}"
    data = request_url_to_dict(url)

    if not isinstance(data, dict) or "images" not in data:
        return data

    images = [
        _normalize_image_fields(i)
        for i in data["images"]
        if filter_by_container_registry(container_type, registry_host, i)
    ]

    sorted_images = _sort_images(images, sort_by_size, sort_by_download)

    if all:
        return sorted_images
    return sorted_images[0] if sorted_images else None
