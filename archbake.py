#!/usr/bin/env python
"""
	ArchBake - Automates the provisioning of Arch Linux Virtual Machines

	Usage:
		archbake.py [<config_file>] --output-image=output_image
		archbake.py --output-image=output_image

"""
try:
	import subprocess
	import sys
	from docopt import docopt
	import os
except ImportError as e:
	print("Failed to import {0}".format(e.name))

def run(cmd):
	"""Syntactic sugar for running a command as current user"""
	subprocess.call(cmd.split())

def sudo_run(cmd):
	"""Syntactic sugar for running a command as sudo"""
	subprocess.call(("sudo {0}".format(cmd)).split())

if __name__ == "__main__":
	#Begin by testing if pre-requisites are installed
	arguments = docopt(__doc__)
	prereqs = ["git"]
	for prereq in prereqs:
		try:
			subprocess.call([prereq],stdout=subprocess.PIPE)
		except FileNotFoundError:
			print("{0} isn't installed. ArchBake needs {0} to function".format(prereq))
			sys.exit(1)
	#Prerequisites are all present, get arch-install-scripts from git
	if os.path.isdir("arch-install-scritps") != True:
		run("git clone git://github.com/falconindy/arch-install-scripts.git")
	
