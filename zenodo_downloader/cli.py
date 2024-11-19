"""
Command-line interface for Zenodo Downloader
"""

import os
import argparse
from concurrent.futures import ThreadPoolExecutor
from .downloader import ZenodoDownloader

def parse_args():
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(
        description='Download files from Zenodo using record ID and access token',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument('record_id', 
                      help='Zenodo record ID to download files from')
    parser.add_argument('-t', '--token',
                      required=True,
                      help='Zenodo access token')
    parser.add_argument('-d', '--directory',
                      default=os.path.join(os.getcwd(), 'downloads'),
                      help='Directory to save downloaded files')
    parser.add_argument('-w', '--workers',
                      type=int,
                      default=5,
                      help='Number of parallel download workers')
    return parser.parse_args()

def main():
    """Main entry point for the command-line interface"""
    args = parse_args()
    downloader = ZenodoDownloader(args.token, args.directory)
    
    # Get list of files in the record
    files = downloader.get_record_files(args.record_id)
    
    if not files:
        print(f"No files found in record {args.record_id}")
        return
    
    print(f"Found {len(files)} files to download from record {args.record_id}")
    print(f"Files will be saved to: {args.directory}")
    print(f"Using {args.workers} parallel download workers")
    
    successful = 0
    failed = 0
    
    # Use ThreadPoolExecutor for parallel downloads
    with ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = list(executor.map(downloader.download_file, files))
        successful = sum(1 for x in futures if x)
        failed = len(files) - successful
    
    print(f"\nDownload Summary:")
    print(f"Successful downloads: {successful}")
    print(f"Failed downloads: {failed}")
    if successful > 0:
        print(f"Files have been saved to: {args.directory}")

if __name__ == "__main__":
    main()
