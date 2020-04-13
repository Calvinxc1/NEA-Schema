import setuptools

with open('README.md') as fh:
    long_description = fh.read()

setuptools.setup(
    name='nea_schema',
    version='0.1.0',
    author='Jason M. Cherry',
    author_email='jcherry@gmail.com',
    description='NEA Toolkit: Database Schema',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/Calvinxc1/NEA-Schema',
    packages=setuptools.find_packages(),
    install_requires=[
        'sqlalchemy >= 1.3, <2',
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: GNU General Public License (GPL)',
        'Operating System :: OS Independent',
        'Development Status :: 2 - Pre-Alpha',
    ],
    python_requires='>= 3.5',
)