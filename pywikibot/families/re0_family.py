"""
This family file was auto-generated by generate_family_file.py script.

Configuration parameters:
  url = https://rezero.fandom.com/zh
  name = re0

Please do not commit this to the Git repository!
"""
from pywikibot import family


class Family(family.Family):  # noqa: D101

    name = 're0'
    langs = {
        'zh': 'rezero.fandom.com',
        'de': 'rezero.fandom.com',
        'en': 'rezero.fandom.com',
        'es': 'rezero.fandom.com',
        'fr': 'rezero.fandom.com',
        'it': 'rezero.fandom.com',
        'nl': 'rezero.fandom.com',
        'pl': 'rezero.fandom.com',
        'pt-br': 'rezero.fandom.com',
        'ru': 'rezero.fandom.com',
        'uk': 'rezero.fandom.com',
    }

    def scriptpath(self, code):
        return {
            'zh': '/zh',
            'de': '/de',
            'en': '',
            'es': '/es',
            'fr': '/fr',
            'it': '/it',
            'nl': '/nl',
            'pl': '/pl',
            'pt-br': '/pt-br',
            'ru': '/ru',
            'uk': '/uk',
        }[code]

    def protocol(self, code):
        return {
            'zh': 'https',
            'de': 'https',
            'en': 'https',
            'es': 'https',
            'fr': 'https',
            'it': 'https',
            'nl': 'https',
            'pl': 'https',
            'pt-br': 'https',
            'ru': 'https',
            'uk': 'https',
        }[code]
