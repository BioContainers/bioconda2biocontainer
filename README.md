# bioconda2biocontainer

*bioconda2biocontainer* includes a series of python scripts and API to query
the Biocontainer registry.

## Scripts

### *bioconda2biocontainer*

This script search the Biocontainer registry and return the image name
for a Bioconda package. The images can be sorted by date, size or number of downloads.

#### Get latest image for bedtools version 2.27.0

```bash
> bioconda2biocontainer --package_name bedtools --package_version 2.27.0
quay.io/biocontainers/bedtools:2.27.0--he513fc3_4
```

#### Get smaller image for bedtools version 2.27.0

```bash
> bioconda2biocontainer --package_name bedtools --package_version 2.27.0 --sort_by_size
quay.io/biocontainers/bedtools:2.27.0--he860b03_3
```

#### Get image with more downloads for bedtools version 2.27.0

```bash
> bioconda2biocontainer --package_name bedtools --package_version 2.27.0 --sort_by_download
quay.io/biocontainers/bedtools:2.27.0--he860b03_3
```

#### List all available images for bedtools version 2.27.0

```bash
> bioconda2biocontainer --package_name bedtools --package_version 2.27.0 --all
image	updated	size	downloads
quay.io/biocontainers/bedtools:2.27.0--he513fc3_4	2019-10-26T00:00:00Z	17332806	0
quay.io/biocontainers/bedtools:2.27.0--he860b03_3	2019-02-03T00:00:00Z	13482660	0
quay.io/biocontainers/bedtools:2.27.0--he941832_2	2018-06-25T00:00:00Z	13652262	0
quay.io/biocontainers/bedtools:2.27.0--1	2018-02-14T00:00:00Z	14094467	0
quay.io/biocontainers/bedtools:2.27.0--0	2017-12-07T00:00:00Z	14087205	0
```

#### List all available versions for bedtools

```bash
> bioconda2biocontainer --package_name bedtools
id	version	url
bedtools-v2.28.0	v2.28.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.28.0
bedtools-v2.27.1dfsg-4-deb	v2.27.1dfsg-4-deb	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.27.1dfsg-4-deb
bedtools-v2.27.0	v2.27.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.27.0
bedtools-v2.26.0dfsg-3-deb	v2.26.0dfsg-3-deb	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.26.0dfsg-3-deb
bedtools-v2.25.0	v2.25.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.25.0
bedtools-2.29.2	2.29.2	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.29.2
bedtools-2.29.1	2.29.1	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.29.1
bedtools-2.29.0	2.29.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.29.0
bedtools-2.28.0	2.28.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.28.0
bedtools-2.27.1	2.27.1	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.27.1
bedtools-2.27.0	2.27.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.27.0
bedtools-2.26.0gx	2.26.0gx	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.26.0gx
bedtools-2.25.0	2.25.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.25.0
bedtools-2.23.0	2.23.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.23.0
bedtools-2.22	2.22	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.22
bedtools-2.20.1	2.20.1	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.20.1
bedtools-2.19.1	2.19.1	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.19.1
bedtools-2.17.0	2.17.0	http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.17.0
```

### biocontainers-search

Search tools in Biocontainers registry and return a TAB separated table with Name, Versions (comma separated),
Description, License and number of pulls. 

#### Search proteomics tools

```bash
> biocontainers-search --search_term proteomics
name	versions	description	license	pulls
augustus	v3.3.2dfsg-2-deb,v3.2.3dfsg-1-deb,3.3.3,3.3.2,3.3,3.2.3,3.2.2,3.1	Augustus is a eukaryotic gene prediction tool. it can integrate evidence, e.g. from rna-seq, ests, proteomics, but can also predict genes ab initio. the ppx extension to augustus can take a protein sequence multiple sequence alignment as input to find new members of the family in a genome. it can be run through a web interface (see https://bio.tools/webaugustus), or downloaded and run locally.	Artistic-1.0	448371
bioconductor-assessorf	1.6.0,1.4.0,1.2.0,1.0.2	Assess Gene Predictions Using Proteomics and Evolutionary Conservation	GPL-3	915
bioconductor-customprodb	1.28.0,1.26.0,1.24.0,1.22.0,1.14.0	Generate customized protein database from ngs data, with a focus on rna-seq data, for proteomics search	Not available	10520
```

#### Search proteomics tools and return JSON data

```bash
> biocontainers-search --search_term proteomics --json
[
    {
        "contains": [],
        "description": "Augustus is a eukaryotic gene prediction tool. it can integrate evidence, e.g. from rna-seq, ests, proteomics, but can also predict genes ab initio. the ppx extension to augustus can take a protein sequence multiple sequence alignment as input to find new members of the family in a genome. it can be run through a web interface (see https://bio.tools/webaugustus), or downloaded and run locally.",
        "id": "augustus",
        "identifiers": [
            "biotools:augustus",
            "PMID:15215400"
        ],
        "license": "Artistic-1.0",
        "name": "augustus",
        "organization": "biocontainers",
        "pulls": 448371,
        "tool_tags": [
            "biology",
            "bioinformatics",
            "c++",
            "commandline",
            "program",
            "calculation",
            "utility",
            "ncurses",
            "analysing",
            "biological-sequence"
        ],
        "tool_url": "https://github.com/Gaius-Augustus/Augustus",
        "toolclass": {
            "description": "CommandLineTool",
            "id": "0",
            "name": "CommandLineTool"
        },
        "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/augustus",
        "versions": [
            {
                "id": "augustus-3.2.3",
                "meta_version": "3.2.3",
                "name": "augustus",
                "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/augustus/versions/augustus-3.2.3"
            },
            {
                "id": "augustus-3.2.2",
                "meta_version": "3.2.2",
                "name": "augustus",
                "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/augustus/versions/augustus-3.2.2"
            },
            ...
```


## Install

```sh
pip install bioconda2biocontainer
```

For development:

```sh
git clone https://github.com/BioContainers/bioconda2biocontainer
cd bioconda2biocontainer
pip install -r requirements/test.txt -e .
```

## Test

Test configuration is defined in the `tox.ini` file and includes `py.test` tests
and `flake8` source code checker.

You can run all of the tests:

```
python setup.py test
```

To run just the `py.test` tests, not `flake8`, and to re-use the current `virtualenv`:

```sh
py.test
```

## API

### Demo

```python
>>> import json
>>> from bioconda2biocontainer.biocontainer import find_package_by_name
>>> tool = find_package_by_name('bedtools')
>>> print(json.dumps(tool, indent=4))
{
    "contains": [],
    "description": "Bedtools is an extensive suite of utilities for comparing genomic features in bed format.",
    "id": "bedtools",
    "identifiers": [
        "biotools:bedtools",
        "PMID:20110278"
    ],
    "license": "GPL-2.0",
    "name": "bedtools",
    "organization": "biocontainers",
    "pulls": 6111180,
    "tool_tags": [
        "genomics"
    ],
    "tool_url": "https://github.com/arq5x/bedtools2",
    "toolclass": {
        "description": "CommandLineTool",
        "id": "0",
        "name": "CommandLineTool"
    },
    "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools",
    "versions": [
        {
            "id": "bedtools-v2.28.0",
            "meta_version": "v2.28.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.28.0"
        },
        {
            "id": "bedtools-v2.27.1dfsg-4-deb",
            "meta_version": "v2.27.1dfsg-4-deb",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.27.1dfsg-4-deb"
        },
        {
            "id": "bedtools-v2.27.0",
            "meta_version": "v2.27.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.27.0"
        },
        {
            "id": "bedtools-v2.26.0dfsg-3-deb",
            "meta_version": "v2.26.0dfsg-3-deb",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.26.0dfsg-3-deb"
        },
        {
            "id": "bedtools-v2.25.0",
            "meta_version": "v2.25.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-v2.25.0"
        },
        {
            "id": "bedtools-2.29.2",
            "meta_version": "2.29.2",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.29.2"
        },
        {
            "id": "bedtools-2.29.1",
            "meta_version": "2.29.1",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.29.1"
        },
        {
            "id": "bedtools-2.29.0",
            "meta_version": "2.29.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.29.0"
        },
        {
            "id": "bedtools-2.28.0",
            "meta_version": "2.28.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.28.0"
        },
        {
            "id": "bedtools-2.27.1",
            "meta_version": "2.27.1",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.27.1"
        },
        {
            "id": "bedtools-2.27.0",
            "meta_version": "2.27.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.27.0"
        },
        {
            "id": "bedtools-2.26.0gx",
            "meta_version": "2.26.0gx",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.26.0gx"
        },
        {
            "id": "bedtools-2.25.0",
            "meta_version": "2.25.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.25.0"
        },
        {
            "id": "bedtools-2.23.0",
            "meta_version": "2.23.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.23.0"
        },
        {
            "id": "bedtools-2.22",
            "meta_version": "2.22",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.22"
        },
        {
            "id": "bedtools-2.20.1",
            "meta_version": "2.20.1",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.20.1"
        },
        {
            "id": "bedtools-2.19.1",
            "meta_version": "2.19.1",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.19.1"
        },
        {
            "id": "bedtools-2.17.0",
            "meta_version": "2.17.0",
            "name": "bedtools",
            "url": "http://api.biocontainers.pro/ga4gh/trs/v2/tools/bedtools/versions/bedtools-2.17.0"
        }
    ]
}
>>>

```
