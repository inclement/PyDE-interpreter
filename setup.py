from setuptools import setup, find_packages
from distutils.extension import Extension
from Cython.Distutils import build_ext

packages = find_packages()

options = {'apk': {'debug': None,
                   'window': None,
                   'requirements': 'sdl2,kivy,python2,pygments',
                   'android-api': 19,
                   'ndk-dir': '/home/asandy/android/crystax-ndk-10.3.2',
                   # 'dist-name': 'pyde',
                   'dist-name': 'pyde_new',
                   'ndk-version': '10.3.2',
                   'package': 'net.inclem.pyde',
                   'permission': 'INTERNET',
                   'service': 'interpreter:interpreter_subprocess/interpreter.py',
                   'arch': 'armeabi-v7a',
                   'icon': 'temp_icon.png',
                   }}
setup(
    name='PyDE interpreter',
    version='0.2',
    description='A Python mobile IDE experiment',
    author='Alexander Taylor',
    author_email='alexanderjohntaylor@gmail.com',
    packages=packages,
    options=options,
    package_data={'pyde': ['*.py', '*.kv'],
                  'pyde/interpreter_subprocess': ['*.py'],
                  'pyde/assets': ['*.ttf', '*.txt']}
)
