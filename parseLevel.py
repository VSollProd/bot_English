import requests
from bs4 import BeautifulSoup

class WordsParser:
    def __init__(self):
        self.urls = {
            'A1': 'https://tefl-tesol-certificate.com/blog/slova-dlya-a1-elementary-nachalnyj-uroven-anglijskogo',
            'A2': 'https://tefl-tesol-certificate.com/blog/slova-dlya-urovnya-anglijskogo-a2-pre-intermediate',
            'B1': 'https://tefl-tesol-certificate.com/blog/slova-dlya-b1-intermediate',
            'B2': 'https://tefl-tesol-certificate.com/blog/slova-urovnya-anglijskogo-b2-upper-intermediate',
            'C1': 'https://tefl-tesol-certificate.com/blog/slova-dlya-urovnya-anglijskogo-c1-advanced-prodvinutyj'
        }

    def parse_words(self, level):
        url = self.urls.get(level)
        if not url:
            return []

        r = requests.get(url)
        bs = BeautifulSoup(r.text, 'html.parser')
        rows = bs.select('div.overflow tr, table.numeric tr')[1:]  # select all rows except the header row

        words_list = [row.text for row in rows]
        return words_list




