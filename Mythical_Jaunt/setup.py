try:
  from setuptools import setup
except ImportError:
  from distutils.core import setup

config = {
  'description' : 'A fantasy adventure game implemented using a map and an engine.',
  'author' : 'Brent Holmes',
  'url' : 'n/a',
  'download_url' : 'n/a',
  'author_email' : 'brentholmes@ku.edu',
  'version' : '0.1',
  'install_requires' : ['nose'],
  'packages' : ['Mythical_Jaunt', 'birth1', 'death', 'doorway', 'elf_kingdom,'
                'forest', 'grove', 'metropolis', 'plains'],
  'scripts' : [],
  'name' : 'Mythical_Jaunt'
}

setup(**config)
