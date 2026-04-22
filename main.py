import shutil
import os
from schema import *
from config import *

def main():
    if os.path.exists('dist'):
        shutil.rmtree('dist')
    shutil.copytree('public', 'dist')

    with open('template.html') as f:
        template = f.read()

    # process

    with open('dist/index.html', 'w') as f:
        f.write(template)

if __name__ == '__main__':
    main()