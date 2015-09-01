from setuptools import setup

setup(name='pytest-repeat',
      version='0.1',
      description='pytest plugin for repeating tests',
      long_description=open('README.rst').read(),
      author='Bob Silverberg',
      author_email='bsilverberg@mozilla.com',
      url='https://github.com/bobsilverberg/pytest-repeat',
      py_modules=['pytest_repeat'],
      entry_points={'pytest11': ['repeat = pytest_repeat']},
      install_requires=['pytest>=2.4.2'],
      license='Mozilla Public License 2.0 (MPL 2.0)',
      keywords='py.test pytest json variables',
      classifiers=[
          'Development Status :: 3 - Alpha',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: Mozilla Public License 2.0 (MPL 2.0)',
          'Operating System :: POSIX',
          'Operating System :: Microsoft :: Windows',
          'Operating System :: MacOS :: MacOS X',
          'Topic :: Software Development :: Quality Assurance',
          'Topic :: Software Development :: Testing',
          'Topic :: Utilities',
          'Programming Language :: Python',
          'Programming Language :: Python :: 2.6',
          'Programming Language :: Python :: 2.7'])