import os
import os.path

from setuptools import find_packages
from setuptools import setup


def readme():
    with open(os.path.join(os.path.dirname(__file__), 'README.md')) as f:
        return f.read()


setup(
    name='bioconda2biocontainer',
    packages=find_packages(where='src'),
    package_dir={
        '': 'src',
    },
    data_files=[('', ['README.md'])],
    version='0.0.1',
    description='Find biocontainer images for Bioconda packages',
    long_description=readme(),
    long_description_content_type='text/markdown',
    license='Public Domain',
    author='Vera Alvarez, Roberto',
    author_email='veraalva' '@' 'ncbi.nlm.nih.gov',
    maintainer='Vera Alvarez, Roberto',
    maintainer_email='veraalva' '@' 'ncbi.nlm.nih.gov',
    url='https://github.com/BioContainers/bioconda2biocontainer',
    install_requires=['requests'],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        'License :: Public Domain',
        'Natural Language :: English',
        'Operating System :: Unix',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Topic :: Scientific/Engineering :: Bio-Informatics'
    ],
    keywords='Biocontainers',
    project_urls={
        'Documentation': 'https://github.com/BioContainers/bioconda2biocontainer/issues',
        'Source': 'https://github.com/BioContainers/bioconda2biocontainer',
        'Tracker': 'https://github.com/BioContainers/bioconda2biocontainer/issues',
    },
    entry_points={
        'console_scripts': [
            'bioconda2biocontainer = bioconda2biocontainer.entry_point:main',
        ],
    }
)
