#!/usr/bin/env python

from setuptools import setup, find_packages

setup(
			name='pyMSScorch',
      version='1.0',
      description='Generate python clients for Microsoft system center orchestrator runbooks',
      author='Jackie Chen',
      author_email='support@jackiechen.org',
      packages=find_packages(),
			install_requires=['pyHyperV'],
     )
