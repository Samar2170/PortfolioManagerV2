import os
from pf_manager.settings import BASE_DIR

def file_handler(file):
    file_path = os.path.join(BASE_DIR, 'Assets', file.name)
    with open(file_path, 'wb') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return file_path