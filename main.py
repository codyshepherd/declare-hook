#!/usr/bin/env python
import click
import jinja2
import os
import yaml


templates_path = os.getcwd() + '/templates/'

@click.command()
@click.argument('yaml_file',
                type=click.Path(exists=True, dir_okay=False, readable=True))
def main(yaml_file):
    with open(yaml_file, 'r') as fh:
        config = yaml.safe_load(fh)

    included_templates = config.get('templates', [])

    master = ''

    template_files = os.listdir('templates/')
    included_template_files = [f for f in template_files
                               if f[:-3] in included_templates]
    for t_file in included_template_files:
        with open(templates_path + t_file, 'r') as fh:
            template_file = fh.read()

        template = jinja2.Template(template_file)

        new = template.render(config)
        master += new

    with open('output.binary', 'w+') as fh:
        fh.write(master)

if __name__ == '__main__':
    declare_image()
