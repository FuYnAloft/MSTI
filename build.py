import json
import os
import shutil
from dataclasses import asdict

from jinja2 import Environment, FileSystemLoader

from config import XXBI


def main() -> None:
    try:
        shutil.rmtree('dist')
    except PermissionError:
        pass
    os.makedirs('dist', exist_ok=True)
    shutil.copytree('public', 'dist', dirs_exist_ok=True)

    env = Environment(loader=FileSystemLoader('.'), autoescape=False)
    template = env.get_template('template.html')

    xxbi_json = json.dumps(asdict(XXBI), ensure_ascii=False)
    html = template.render(xxbi_json=xxbi_json)

    with open('dist/index.html', 'w', encoding='utf-8') as f:
        f.write(html)

    print("构建成功")


if __name__ == '__main__':
    main()
