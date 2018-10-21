from distutils.core import setup

setup(name='funniest',
      version='0.1',
      description='Plot 2-dimensional arrays in parallel coordinates',
      url='https://github.com/mancap314/paracoord',
      author='Manuel Capel',
      author_email='manuel.capel82@gmail.com   ',
      license='MIT',
      packages=['paracoord'],
      install_requires=[
          'numpy',
          'matplotlib'
          'itertools'
      ],
      zip_safe=False)
