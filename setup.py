import setuptools

with open('README.md', 'r') as f:
    long_description = f.read()

setuptools.setup(
    name='paracoord',
    version='0.1',
    author='Manuel Capel',
    author_email='manuel.capel82@gmail.com',
    description='Parallel Coordinates plotting',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/mancap314/paracoord',
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
