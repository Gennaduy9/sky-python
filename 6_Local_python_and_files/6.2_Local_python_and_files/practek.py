#from os.path import abspath, dirname, join as joinpath

#BASE_DIR = dirname(dirname(abspath(__file__)))
#TEMPLATES_DIR = joinpath(BASE_DIR, 'templates')


#from pathlib import Path

#file_contents = [
#    path.read_text()
#    for path in Path.cwd().rglob('*.py')
#]

import os
import os.path

def make_editorconfig(dir_path):
    """Create .editorconfig file in given directory and return filename."""
    filename = os.path.join(dir_path, '.editorconfig')
    if not os.path.exists(filename):
        os.makedirs(dir_path, exist_ok=True)
        open(filename, mode='wt').write('')
    return filename

make_editorconfig(dir_path)