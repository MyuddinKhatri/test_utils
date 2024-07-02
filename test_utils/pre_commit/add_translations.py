import os
import logging
import argparse
import pathlib
from typing import Sequence

# try:
# 	from frappe.translate import get_untranslated, update_translations
# except Exception as e:
# 	raise(e)

logging.basicConfig(filename='hook.log', level=logging.INFO, format='%(message)s')
logger = logging.getLogger(__name__)

# def add_translations(lang, app):
# 	untranslated_file = "untranslated_strings"
# 	translated_file = "translated_strings"
# 	get_untranslated(lang=lang, untranslated_file=untranslated_file, app=app)
# 	update_translations(lang=lang, untranslated_file=untranslated_file, translated_file=translated_file, app=app)


def main(argv: Sequence[str] = None):
	parser = argparse.ArgumentParser()
	parser.add_argument('filenames', nargs='*')
	parser.add_argument('--lang', action='append', help='Language to translate strings')
	parser.add_argument('--app', action='append', help='App to get untranslated string and translate them')
	args = parser.parse_args(argv)

	print("===============================================", pathlib.Path().resolve())
	lang = args.lang[0]
	app = args.app[0]
	# add_translations(lang, app)