# roblox-oof-replacer

This script replaces the current death sound in Roblox with the classic "oof" sound.

## What It Does

- Locates your Roblox installation.
- Finds the current version folder.
- Replaces the default death sound with the old "OOF" sound.
- Can be re-run after each Roblox update.

## Setup Instructions

1. Clone or download this repository.
2. Make sure you have Python installed.
3. Download or place your old **oof sound file** (e.g. `ouch.ogg`) in the same folder as the script.
4. Open `oof.py` in a text editor.
5. Edit the `versions_path` variable with your actual Roblox path:

    ```python
    versions_path = r'C:\Users\YourUsername\AppData\Local\Roblox\Versions'
    ```

6. Save and run the script:

    ```bash
    python oof.py
    ```

---

## How to Use

- Every time Roblox updates, the sound files may be reset.
- Simply **re-run the script** after updates to restore the "OOF".


## Disclaimer
This project includes audio content that is not owned by the author.
All rights to the "OOF" sound belong to their respective copyright holders.
This repository is for educational and archival purposes only.
