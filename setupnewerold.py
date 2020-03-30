from setuptools import setup

# with open("README.md", 'r') as f:
#     long_description = f.read()

setup(name = "ignition",
      version = 0.0.2,
      description = "Hit the ground running on your fresh Ubuntu installation.",
      author = "Josh L",
      author_email = "sillynoodle63@gmail.com",
      #url = na.xyz,
      packages = ['ignition'],
      scripts = ['Main.py'],
      license = GPL-3
      #cmdclass = { 'test': TestCommand}
)
