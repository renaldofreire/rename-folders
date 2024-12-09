import os
import re

def rename_folders(path_dir):
    for folder in os.listdir(path_dir):
        folder_full_path = os.path.join(path_dir, folder)
        
        if os.path.isdir(folder_full_path):
            folder_style = r'\((\d{4})\)\s*(.+?)\s*\[.+\]'
            
            corresp = re.match(folder_style, folder)
            
            if corresp:
                year = corresp.group(1)
                album_name = corresp.group(2).split('-')[-1].strip()
                
                new_name = f"{year} - {album_name}"
                
                new_path = os.path.join(path_dir, new_name)
                
                os.rename(folder_full_path, new_path)
                print(f"Nome ANTERIOR: {folder} -> Nome ATUAL: {new_name}")

# to use
path_dir = '/mnt/disk1/Music/Name/'
rename_folders(path_dir)
