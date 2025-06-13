import os
import shutil

# Path to your Roblox Versions folder
versions_path = r'[ENTER HERE]\AppData\Local\Roblox\Versions'

# Path to your preferred ouch.ogg file
preferred_ouch_file = r'[OUCH.OGG LOCATION HERE]'

# Function to get the latest version folder that contains a 'sounds' folder
def get_latest_version_folder_with_sounds():
    folders = [f for f in os.listdir(versions_path) if os.path.isdir(os.path.join(versions_path, f))]
    folders.sort(key=lambda x: os.path.getmtime(os.path.join(versions_path, x)), reverse=True)
    
    for folder in folders:
        sounds_folder = os.path.join(versions_path, folder, 'content', 'sounds')
        if os.path.exists(sounds_folder):
            return folder  # Return the first folder that has a sounds folder
    
    return None  # Return None if no valid folder is found

# Replace ouch.ogg in the latest version folder with a sounds folder or add it if it's missing
def replace_ouch_file():
    latest_version_folder = get_latest_version_folder_with_sounds()
    
    if not latest_version_folder:
        print("No Roblox version folder with a sounds folder found.")
        return
    
    sounds_folder = os.path.join(versions_path, latest_version_folder, 'content', 'sounds')
    ouch_file_path = os.path.join(sounds_folder, 'ouch.ogg')
    
    # Add or replace the ouch.ogg file
    shutil.copy(preferred_ouch_file, ouch_file_path)
    print(f"Added or replaced ouch.ogg in: {ouch_file_path}")

# Run the replacement
replace_ouch_file()
