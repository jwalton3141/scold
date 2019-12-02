try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='scold',
    packages=['scold'],
    version='1.0',
    description='Scold it',
    long_description='Like [praise](https://github.com/funtion/praise), but when you (or your colleagues)
have been bad.',
    author='Jack Walton',
    author_email='jwalton3141@gmail.com',
    url='https://github.com/jwalton3141/scold',
    download_url='https://github.com/jwalton3141/scold/archive/1.0.tar.gz',
    keywords=['scold', 'logging'],
    classifiers=[],
    test_suite='nose.collector',
    tests_require=['nose']
)
