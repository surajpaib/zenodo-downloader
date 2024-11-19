"""
Core functionality for downloading files from Zenodo
"""

import os
import requests
from tqdm import tqdm

class ZenodoDownloader:
    """A class to handle downloading files from Zenodo records"""
    
    def __init__(self, access_token, output_dir):
        """
        Initialize the downloader
        
        Args:
            access_token (str): Zenodo access token
            output_dir (str): Directory to save downloaded files
        """
        self.access_token = access_token
        self.output_dir = output_dir
        self.headers = {
            'Authorization': f'Bearer {access_token}',
        }
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)
    
    def get_record_files(self, record_id):
        """
        Get list of files for a specific record
        
        Args:
            record_id (str): Zenodo record ID
            
        Returns:
            list: List of file metadata dictionaries
        """
        metadata_url = f"https://zenodo.org/api/records/{record_id}"
        try:
            metadata_response = requests.get(metadata_url, headers=self.headers)
            metadata_response.raise_for_status()
            return metadata_response.json().get('files', [])
        except requests.exceptions.RequestException as e:
            print(f"Error fetching record {record_id}: {str(e)}")
            return []
    
    def download_file(self, file_data):
        """
        Download a single file using its metadata
        
        Args:
            file_data (dict): File metadata from Zenodo API
            
        Returns:
            bool: True if download was successful, False otherwise
        """
        try:
            filename = file_data['key']
            download_url = file_data['links']['self']
            
            print(f"Downloading: {filename}")
            response = requests.get(download_url, headers=self.headers, stream=True)
            response.raise_for_status()
            
            total_size = int(response.headers.get('content-length', 0))
            output_path = os.path.join(self.output_dir, filename)
            
            with open(output_path, 'wb') as fd:
                with tqdm(total=total_size, unit='B', unit_scale=True, desc=filename) as pbar:
                    for chunk in response.iter_content(chunk_size=1024*1024):
                        if chunk:
                            fd.write(chunk)
                            pbar.update(len(chunk))
            print(f"Successfully downloaded: {filename}")
            return True
            
        except requests.exceptions.RequestException as e:
            print(f"Error downloading {filename}: {str(e)}")
            return False
