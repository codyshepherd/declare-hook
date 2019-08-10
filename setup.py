import os
from setuptools import find_packages, setup

reqs_path = os.path.join(os.path.dirname(__file__), 'requirements.txt')

with open(reqs_path, 'r') as req_file:
    dependencies = req_file.readlines()

setup(
    name='declare_hook',
    version='0.1.0',
    license='Proprietary',
    author='Cody Shepherd',
    author_email='cody.shepherd@gmail.com',
    description='Generate livecd-rootfs hook from a yaml',
    long_description=__doc__,
    packages=find_packages(exclude=['tests']),
    include_package_data=True,
    zip_safe=False,
    platforms='any',
    install_requires=dependencies,
    entry_points={
        'console_scripts': [
            'declare-hook = main:main',
        ],
    },
)
