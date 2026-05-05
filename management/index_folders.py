import os
from pathlib import Path
import argparse

parser = argparse.ArgumentParser(
        prog = 'Obsidian Indexer',
        description = 'Recursively add index files to a vault so hugo recognizes them as url subdirectories'
        )

parser.add_argument('dir', help = "directory to index. default = 'vault/'")

def index_vault(wdir):
    abs_path = Path(wdir).absolute()
    with open(abs_path / '__index__.md', 'w') as f:
        f.write(' ')

    sub_folders = [x for x in os.listdir(abs_path) if (os.path.isdir(abs_path / x) and x[0] != '.')]
    [index_vault(abs_path / x) for x in sub_folders]
    return

args = parser.parse_args()
index_vault(args.dir if args.dir else 'vault')

if __name__ == '__main__':
    index_vault('vault')

