from setuptools import setup, find_packages

with open('requirements.txt') as f:
    INSTALL_REQUIRES = [l.strip() for l in f.readlines() if l]

setup(name='pydungeon',
      version='0.1',
      author='Viren Nadkarni',
      author_email='viren@outlook.com',
      install_requires=INSTALL_REQUIRES,
      packages=find_packages(),
      entry_points={
          'gui_scripts': ['pydungeon = pydungeon.__main__:main']
      }
)
