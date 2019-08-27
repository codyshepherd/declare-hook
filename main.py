#!/usr/bin/env python
import click
import jinja2
import os
import yaml

templates_path = os.getcwd() + '/templates/'
LOG_FILE = 'run.log'
if os.path.isfile(LOG_FILE):
    os.remove(LOG_FILE)
if os.path.isfile("output.binary"):
    os.remove("output.binary")

def log(text):
    with open(LOG_FILE, 'a+') as fh:
        fh.write(text + '\n')

@click.command()
@click.argument('yaml_file',
                type=click.Path(exists=True, dir_okay=False, readable=True))
def main(yaml_file):
    with open(yaml_file, 'r') as fh:
        config = yaml.safe_load(fh)

    included_templates = config.get('templates', [])

    master = ''

    template_files = os.listdir('templates/')
    log("Template files:\n{}".format(template_files))
    included_template_files = [f for f in template_files
                               if f[4:-3] in included_templates]
    included_template_files = sorted(included_template_files)
    log("Included Templates:\n{}".format(included_template_files))
    for t_file in included_template_files:
        log("Opening template {}".format(t_file))
        with open(templates_path + t_file, 'r') as fh:
            template_file = fh.read()

        template = jinja2.Template(template_file)

        new = template.render(config)
        log("Appending:\n{}".format(new))

        with open('output.binary', 'a+') as fh:
            fh.write(new + '\n')

if __name__ == '__main__':
    main()
