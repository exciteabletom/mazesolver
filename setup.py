#!/usr/bin/env python3
from setuptools import setup, find_packages
import sys
from mazesolver import strings

print(strings.version)
with open("./README.md", encoding="utf-8") as readme:
	long_description = readme.read()

setup(
	name="mazesolver",
	version=strings.version,

	description="A shortest-path maze solving algorithm for image-based mazes.",
	long_description=long_description,
	long_description_content_type="text/markdown",

	url="https://github.com/exciteabletom/mazesolver",
	author="Tommy Dougiamas",
	author_email="tom@digitalnook.net",

	classifiers=[
		# "Development Status :: 5 - Stable",

		"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

		"Programming Language :: Python :: 3"

	],

	entry_points={
		"console_scripts": ["mazesolver = mazesolver.__main__:main"],
	},

	keywords="maze algorithm image solve",

	packages=["mazesolver"],

	python_requires=">=3.5",

	install_requires=["Pillow>=6.0", "progress>=1.5"]
)
