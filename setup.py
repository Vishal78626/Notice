from setuptools import setup, find_packages

with open("requirements.txt") as f:
	install_requires = f.read().strip().split("\n")

# get version from __version__ variable in notice/__init__.py
from notice import __version__ as version

setup(
	name="notice",
	version=version,
	description="Notice",
	author="SDC",
	author_email="sdc@example.com",
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
