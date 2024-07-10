import os
import shutil
from typing import List, Dict

from proj.status import ExitStatus
from jinja2 import Environment, FileSystemLoader, select_autoescape

from proj import utils
from pathlib import Path


class Project:
    def __init__(self, project_name: str):
        self.project_name = project_name

    def render(self, project_type: str, render_datas: List[Dict], direct_copy_datas: List[Dict]):
        project_path = Path(os.path.join(os.getcwd(), self.project_name))
        project_path.mkdir(parents=True, exist_ok=False)
        os.chdir(project_path)

        template_path = os.path.join(utils.get_template_path(), project_type)
        env = Environment(loader=FileSystemLoader(template_path), autoescape=select_autoescape())

        for item in render_datas:
            template = env.get_template(item['tpl_file'])
            content = template.render(item['render_data'])

            if 'final_file' in item:
                final_file = item['final_file']
            else:
                final_file = Path(item['tpl_file']).stem
            file = open(final_file, 'w')

            file.write(content)
            file.close()

        for item in direct_copy_datas:
            shutil.copyfile(os.path.join(template_path, item['tpl']), item['final'])
