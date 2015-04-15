#!/usr/bin/env python
import codecs
import os

from setuptools import setup


def read(*parts):
    filename = os.path.join(os.path.dirname(__file__), *parts)
    with codecs.open(filename, encoding='utf-8') as fp:
        return fp.read()


setup(
    name='django-login-canary',
    version='0.0.0',
    description='django-login-canary is a reusable Django application to notify users upon successful and failed logins.',
    long_description=read('README.rst'),
    author='Markus Holtermann',
    author_email='info@markusholtermann.eu',
    url='http://github.com/MarkusH/django-login-canary',
    license='MIT',
    packages=[
        'login_canary',
        'login_canary.migrations',
    ],
    package_data={
        'login_canary': [
            'locale/*/LC_MESSAGES/*',
            'templates/login_canary/*',
        ]
    },
    install_requires=[
        'Django>=1.8',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
        'Framework :: Django :: 1.8',
    ],
    zip_safe=False
)
