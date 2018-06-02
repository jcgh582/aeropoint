from setuptools import setup

setup(name='aeropoint',
      version='0.0.1',
      description='Coding Challenge',
      author='Jonathon Hill',
      author_email='jcgh582@gmail.com',
      packages=['aeropoint'],
      test_suite='nose.collector',
      tests_require=['nose'],
      entry_points={
          'console_scripts': [
              'grab_data = aeropoint.__main__:main'
          ]
      })
