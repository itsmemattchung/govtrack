from setuptools import setup

setup(
    name='govtrack',
    packages=['govtrack', 'govtrack.bills'],
    description='govtrack.us python wrapper',
    version='0.0.1',
    author='Matt Chung',
    author_email='matt@itsmemattchung.com',
    install_requires=['requests'],
    license='MIT'
)
