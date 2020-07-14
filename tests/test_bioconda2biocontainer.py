import unittest

from bioconda2biocontainer.biocontainer import find_latest_image
from bioconda2biocontainer.biocontainer import find_package_by_name
from bioconda2biocontainer.biocontainer import find_package_by_term


class TestSet(unittest.TestCase):

    def test_find_package_by_name(self):
        tool = find_package_by_name('bedtools')
        assert tool['id'] == 'bedtools'

    def test_find_latest_image(self):
        images = find_latest_image('bedtools', '2.27.0', False, False, False, 'Docker', 'quay.io')
        assert type(images) == dict

    def test_find_latest_image_all(self):
        images = find_latest_image('bedtools', '2.27.0', True, False, False, 'Docker', 'quay.io')
        flag = False
        for i in images:
            if i['updated'] == '2019-10-26T00:00:00Z':
                flag = True
                assert i['image_name'] == 'quay.io/biocontainers/bedtools:2.27.0--he513fc3_4'
        assert flag

    def test_find_package_by_name_status_code(self):
        tool = find_package_by_name('bedtoolss')
        assert tool == 204

    def test_find_latest_image_sort_by_size(self):
        images = find_latest_image('bedtools', '2.27.0', True, True, False, 'Docker', 'quay.io')
        flag = False
        for i in images:
            if i['updated'] == '2019-10-26T00:00:00Z':
                flag = True
                assert i['image_name'] == 'quay.io/biocontainers/bedtools:2.27.0--he513fc3_4'
        assert flag

    def test_find_latest_image_sort_by_downloads(self):
        images = find_latest_image('bedtools', '2.27.0', True, False, True, 'Docker', 'quay.io')
        flag = False
        for i in images:
            if i['updated'] == '2019-10-26T00:00:00Z':
                flag = True
                assert i['image_name'] == 'quay.io/biocontainers/bedtools:2.27.0--he513fc3_4'
        assert flag

    def test_find_latest_image_status_code(self):
        images = find_latest_image('bedtoolss', '2.27.0', True, False, True, 'Docker', 'quay.io')
        assert images == 204

    def test_search_tool(self):
        data = find_package_by_term('proteomics')
        assert type(data) == list
