from setuptools import setup

MAJOR_VERSION = '0'
MINOR_VERSION = '0'
MICRO_VERSION = '5'
VERSION = "{}.{}.{}".format(MAJOR_VERSION, MINOR_VERSION, MICRO_VERSION)

setup(name='gittraffic',
      version=VERSION,
      description='Follow your git traffic per package in a github repo',
      url='https://github.com/kootenpv/gittraffic',
      author='Pascal van Kooten',
      author_email='kootenpv@gmail.com',
      license='GPL',
      packages=['gittraffic'],
      install_requires=[
          'lxml', 'datetime', 'selenium'
      ],
      entry_points={
          'console_scripts': ['gittraffic = gittraffic.gittraffic:main']
      },
      classifiers=[
          'Environment :: Console',
          'Intended Audience :: Developers',
          'Intended Audience :: Customer Service',
          'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
          'Operating System :: Microsoft',
          'Operating System :: MacOS :: MacOS X',
          'Operating System :: Unix',
          'Operating System :: POSIX',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.3',
          'Programming Language :: Python :: 3.4',
          'Topic :: Software Development',
          'Topic :: Software Development :: Build Tools',
          'Topic :: Software Development :: Debuggers',
          'Topic :: Software Development :: Libraries',
          'Topic :: Software Development :: Libraries :: Python Modules',
          'Topic :: System :: Software Distribution',
          'Topic :: Utilities'
      ],
      zip_safe=False,
      platforms='any')
