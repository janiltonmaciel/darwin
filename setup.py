# encoding: utf-8

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='darwin',
    version='0.1',
    url='https://github.com/janiltonmaciel/darwin',
    author='Janilton Maciel',
    author_email='janilton@gmail.com',
    packages=find_packages(),
    license='GPL',
    description='Uma coleção de funcionalidades para deploy via fabric',
    install_requires=['passlib', 'cryptography'],
    include_package_data=True,
    test_suite='werkzeug.testsuite.suite',
    zip_safe=False,
    platforms='any'
)

