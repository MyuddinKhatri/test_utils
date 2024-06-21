import argparse
import logging
from typing import Sequence
try:
	from frappe.translate import get_untranslated
except Exception as e:
	raise (e)


logging.basicConfig(filename='hook.log', level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

def add_translations(lang, app):
	logger.info(f"In the fn")
	get_untranslated(lang, f"../apps/{app}/random.txt", app)

def main(argv: Sequence[str] = None):
	print("=================HEY")
	logger.info(f"In the main")
	parser = argparse.ArgumentParser()
	parser.add_argument('filenames', nargs='*')
	parser.add_argument('--app', action='append', help='App to execute pre-commit hooks on')
	parser.add_argument('--lang', action='append', help='Language for translation')
	args = parser.parse_args(argv)

	app = "beam"
	lang = "en"
	if app:
		add_translations(lang, app)