# encoding: utf-8

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup, find_packages

setup(
    name='darwin',
    version='1.0.3',
    url='https://github.com/janiltonmaciel/darwin',
    author='Janilton Maciel',
    author_email='janilton@gmail.com',
    packages=find_packages(),
    license='GPL',
    description='Uma coleção de funcionalidades para deploy via fabric',
    install_requires=['passlib>=1.6.2', 'cryptography>=0.9.1'],
    include_package_data=True,
    zip_safe=False,
    platforms='any'
)

