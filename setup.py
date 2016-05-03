import os
from setuptools import setup, find_packages

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]

os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(name='pydungeon',
      version='0.1',
      author='Viren Nadkarni',
      author_email='viren@outlook.com',
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      include_package_data=True,
      zip_safe=False,
      entry_points={
          'console_scripts': ['pydungeon = pydungeon.__main__:main']
      }
)
