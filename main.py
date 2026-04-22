import shutil
import os

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