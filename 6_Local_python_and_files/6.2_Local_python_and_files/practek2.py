from collections import defaultdict
from hashlib import md5
from pathlib import Path

def find_files(filepath):
    for path in Path(filepath).rglob('*'):
        if path.is_file():
            yield path

file_hashes = defaultdict(list)
for path in find_files(Path.cwd()):
    file_hash = md5(path.read_bytes()).hexdigest()
    file_hashes[file_hash].append(path)

for paths in file_hashes.values():
    if len(paths) > 1:
        print("Duplicate files found:")
        print(*paths, sep='\n')