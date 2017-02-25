#!/usr/bin/env python

from distutils.core import setup

setup(name='my_utils',
      version='0.1.0',
      description='Several utilify functions mainly for personal uses',
      author='Yuichi Shiraishi',
      author_email='friend1ws@gamil.com',
      url='https://github.com/friend1ws/my_utils',
      package_dir = {'': 'lib'},
      packages=['my_utils'],
      scripts=['my_utils'],
      license='GPL-3'
     )

