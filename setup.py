from setuptools import setup

# with open("README.md", 'r') as f:
#     long_description = f.read()

setup(
   name='ignition',
   version='0.0.2',
   description='Hit the ground running on your fresh Ubuntu installation.',
   license="GPL 3+",
   long_description="The Linux world is full of apps. You could be looking for an app that does something, only to find that there are literally hundreds of options. Ignition will show you common apps for certain categories and explain their little nuances in an easy format. Just choose the ones to install, and Ignition will start the engine.",
   author='Josh L',
#    author_email='foomail@foo.com',
#    url="http://www.foopackage.com/",
   packages=['ignition'],  #same as name
   install_requires=['figlet'], #external packages as dependencies
#    scripts=[
#             'scripts/cool',
#             'scripts/skype',
#            ]
)