from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

conda_env_file = "environment.yml"
readme_file = "README.md"
pip_req_file = "requirements.txt"

def read(fname):
    with open(path.join(here,fname)) as fp:
        content = fp.read()
    return content

# Get the long description from the README file
long_description = read(readme_file)

changelog = read(readme_file).splitlines()
for i,line in enumerate(changelog):
    if line.startswith('Change-Log'):
        line = changelog[i+1]
        j = 1
        while line.strip()=='' or line.startswith('---'):
            j += 1
            line = changelog[i+j]
        version = line.strip('# ')
        break

# get the dependencies and installs
all_reqs = []
all_reqs += read(pip_req_file).splitlines()

install_requires = [x.strip() for x in all_reqs if 'git+' not in x]
dependency_links = [x.strip() for x in all_reqs if x.startswith('git+')]

setup(
    name='raypy2d',
    version_format='{tag}.dev{commitcount}+{gitsha}',
    setup_requires=['setuptools-git-version','pytest-runner'],
    description='A simple simulation for 2D arrangments of basic optical elements',
    long_description=long_description,
    classifiers=[
      'Development Status :: 3 - Alpha',
      'Intended Audience :: Developers',
      'Programming Language :: Python :: 3',
    ],
    entry_points={'console_scripts': []},
    keywords='',
    packages=find_packages(exclude=['docs', 'tests*']),
    include_package_data=True,
    author='Tobias Schoch',
    install_requires=install_requires,
    tests_require=['pytest'],
    dependency_links=dependency_links,
    author_email='tobias.schoch@vtxmail.ch'
)
