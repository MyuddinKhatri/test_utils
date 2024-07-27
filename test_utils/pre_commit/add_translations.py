import argparse
import os
import sys
import subprocess
from typing import Sequence

def activate_frappe_env():
	frappe_bench_path = "/path/to/frappe-bench"
	env_activate_script = os.path.join(frappe_bench_path, "env", "bin", "activate")

	# Check if frappe-bench exists and has the required directories
	if os.path.exists(frappe_bench_path) and \
	   os.path.isdir(os.path.join(frappe_bench_path, "sites")) and \
	   os.path.isdir(os.path.join(frappe_bench_path, "env")) and \
	   os.path.isdir(os.path.join(frappe_bench_path, "apps")):

		if os.path.exists(env_activate_script):
			# Activate the virtual environment
			command = f"source {env_activate_script} && python3 {' '.join(sys.argv)}"
			subprocess.check_call(command, shell=True)
		else:
			print("Virtual environment activation script not found.")
			sys.exit(1)
	else:
		print("Frappe-bench environment not found or incomplete.")
		sys.exit(1)

# Activate Frappe environment before importing frappe
activate_frappe_env()

try:
	from frappe.translate import get_untranslated, update_translations
except Exception as e:
	raise(e)

def add_translations(lang, app):
	untranslated_file = "untranslated_strings"
	translated_file = "translated_strings"
	get_untranslated(lang=lang, untranslated_file=untranslated_file, app=app)
	update_translations(lang=lang, untranslated_file=untranslated_file, translated_file=translated_file, app=app)

def main(argv: Sequence[str] = None):
	parser = argparse.ArgumentParser()
	parser.add_argument('filenames', nargs='*')
	parser.add_argument('--lang', action='append', help='Language to translate strings')
	parser.add_argument('--app', action='append', help='App to get untranslated string and translate them')
	args = parser.parse_args(argv)

	lang = args.lang[0]
	app = args.app[0]
	add_translations(lang, app)
