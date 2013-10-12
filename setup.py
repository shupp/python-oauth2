from setuptools import setup

VERSION = "0.2.0"

setup(name="python-oauth2",
      version=VERSION,
      description="OAuth 2.0 provider for python",
      long_description=open("README.rst").read(),
      author="Markus Meyer",
      author_email="hydrantanderwand@gmail.com",
      url="https://github.com/wndhydrnt/python-oauth2",
      packages = ["oauth2", "oauth2.test"],
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
    ]
)
