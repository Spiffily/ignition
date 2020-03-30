from setuptools import setup

# with open("README.md", 'r') as f:
#     long_description = f.read()

setup(name = "ignition",
      version = ignition.__version__,
      description = ignition.__description__,
      author = ignition.__author__,
      author_email = ignition.__author_email__,
      url = ignition.__homepage__,
      packages = ['ignition'],
      scripts = ['Main.py'],
      license = GPL-3
      #cmdclass = { 'test': TestCommand}
)
