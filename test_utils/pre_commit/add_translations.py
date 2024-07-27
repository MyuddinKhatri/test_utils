import argparse
import os
import pathlib
import sys
import subprocess
from typing import Sequence

def activate_frappe_env(frappe_bench_path):
	env_activate_script = os.path.join(frappe_bench_path, "env", "bin", "activate")

	# Check if frappe-bench exists and has the required directories
	if os.path.exists(frappe_bench_path) and \
	   os.path.isdir(os.path.join(frappe_bench_path, "sites")) and \
	   os.path.isdir(os.path.join(frappe_bench_path, "env")) and \
	   os.path.isdir(os.path.join(frappe_bench_path, "apps")):

		if os.path.exists(env_activate_script):
			# Activate the virtual environment
			command = "source env/bin/activate"
			subprocess.run(command, shell=True, executable='/bin/bash', cwd=frappe_bench_path)
		else:
			print("Virtual environment activation script not found.")
			sys.exit(1)
	else:
		print("Frappe-bench environment not found or incomplete.")
		sys.exit(1)

def add_translations(lang, app, frappe_bench_path):
	untranslated_file = "untranslated_strings"
	translated_file = "translated_strings"

	# Run get_untranslated command
	command_get_untranslated = f"python -c 'from frappe.translate import get_untranslated; get_untranslated(lang=\"{lang}\", untranslated_file=\"{untranslated_file}\", app=\"{app}\")'"
	subprocess.run(command_get_untranslated, shell=True, executable='/bin/bash', cwd=frappe_bench_path)

	# Run update_translations command
	command_update_translations = f"python -c 'from frappe.translate import update_translations; update_translations(lang=\"{lang}\", untranslated_file=\"{untranslated_file}\", translated_file=\"{translated_file}\", app=\"{app}\")'"
	subprocess.run(command_update_translations, shell=True, executable='/bin/bash', cwd=frappe_bench_path)

def main(argv: Sequence[str] = None):
	parser = argparse.ArgumentParser()
	parser.add_argument('filenames', nargs='*')
	parser.add_argument('--lang', action='append', help='Language to translate strings')
	parser.add_argument('--app', action='append', help='App to get untranslated string and translate them')
	args = parser.parse_args(argv)

	frappe_bench_path = pathlib.Path().resolve().parent.parent

	# Activate Frappe environment
	activate_frappe_env(frappe_bench_path)

	lang = args.lang[0]
	app = args.app[0]

	# Add translations
	add_translations(lang, app, frappe_bench_path)
