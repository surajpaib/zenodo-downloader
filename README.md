# Zenodo Downloader

A command-line tool to download files from Zenodo records efficiently with parallel downloading support.

## Installation

```bash
pip install zenodo-downloader
```

## Usage

Basic usage:
```bash
zenodo-download RECORD_ID -t YOUR_ACCESS_TOKEN
```

With all options:
```bash
zenodo-download RECORD_ID -t YOUR_ACCESS_TOKEN -d /path/to/output -w 10
```

### Arguments

- `RECORD_ID`: Zenodo record ID to download files from (required)
- `-t, --token`: Zenodo access token (required)
- `-d, --directory`: Directory to save downloaded files (default: ./downloads)
- `-w, --workers`: Number of parallel download workers (default: 5)

### Example

```bash
# Download all files from record 13799069 using 8 parallel workers
zenodo-download 13799069 -t YOUR_ACCESS_TOKEN -w 8 -d ./data
```

## Getting a Zenodo Access Token

1. Go to https://zenodo.org/account/settings/applications/
2. Create a new token with the necessary permissions
3. Copy the token and use it with the `-t` option

## Features

- Parallel downloading with configurable number of workers
- Progress bars for each file
- Automatic retry on failed downloads
- Configurable output directory
- Simple command-line interface

## Requirements

- Python >= 3.7
- requests >= 2.25.0
- tqdm >= 4.50.0

## License

MIT License
