import os
import requests

# --- CONFIGURATION ---
NEXTCLOUD_URL = "http://procarpel.ddns.net:4996"
USERNAME = "fgonzalez"
APP_PASSWORD = "YkAWs-68GaA-HDEPz-jfjzb-DfMNZ"

# Paths
LOCAL_FILE_PATH = "Tasas.json"
# Note: Ensure the target directory exists on Nextcloud
REMOTE_FILE_PATH = "Documents/_Tasas/Tasas.json" 

# --- EXECUTION ---
def upload_or_update_nextcloud_file(local_path, remote_path):
    # Construct the standard WebDAV URL for Nextcloud
    webdav_url = f"{NEXTCLOUD_URL}/remote.php/dav/files/{USERNAME}/{remote_path}"
    
    # Read the local binary data
    if not os.path.exists(local_path):
        print(f"Error: Local file {local_path} does not exist.")
        return

    with open(local_path, "rb") as file_data:
        print(f"Uploading {local_path} to Nextcloud...")
        
        # Send HTTP PUT request to create or update the file
        response = requests.put(
            webdav_url,
            auth=(USERNAME, APP_PASSWORD),
            data=file_data
        )
        
    # Evaluate response status codes
    if response.status_code in [201, 204]:
        # 201 = Created (New file), 204 = No Content (Successfully updated file)
        print("Success: File uploaded/updated successfully!")
    else:
        print(f"Failed: HTTP Status {response.status_code}")
        print(response.text)

if __name__ == "__main__":
    upload_or_update_nextcloud_file(LOCAL_FILE_PATH, REMOTE_FILE_PATH)
