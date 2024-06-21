import os
import logging
import argparse
import pathlib
from typing import Sequence

logging.basicConfig(filename='hook.log', level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def setup_frappe():
	bench_path = pathlib.Path().resolve().parent.parent
	os.environ['FRAPPE_SITE_NAME'] = 'localhost.demand'
	os.environ['FRAPPE_BENCH_PATH'] = str(bench_path)
	import frappe
	frappe.init(site=os.environ['FRAPPE_SITE_NAME'])
	frappe.connect()
	return frappe

def add_translations(frappe, lang, app):
	logger.info(f"In the fn")
	from frappe.translate import get_untranslated
	get_untranslated(lang, f"../apps/{app}/random.txt", app)

def main(argv: Sequence[str] = None):
	logger.info(f"In the main")
	parser = argparse.ArgumentParser()
	parser.add_argument('filenames', nargs='*')
	parser.add_argument('--app', action='append', help='App to execute pre-commit hooks on')
	parser.add_argument('--lang', action='append', help='Language for translation')
	args = parser.parse_args(argv)

	app = "beam"  # Default app
	lang = "en"   # Default language
	if app:
		frappe = setup_frappe()
		try:
			add_translations(frappe, lang, app)
		finally:
			frappe.destroy()

if __name__ == '__main__':
	main()