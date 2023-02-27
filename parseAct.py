

class ParseAct():
    def __init__(self):
        self.file_1 = open('economic.txt', 'r', encoding='utf-8').read()
        self.file_2 = open('medicine.txt', 'r', encoding='utf-8').read()
        self.file_3 = open('politics.txt', 'r', encoding='utf-8').read()
        self.file_4 = open('art.txt', 'r', encoding='utf-8').read()
        self.file_5 = open('IT.txt', 'r', encoding='utf-8').read()
    def parse_economic(self):
        economic = self.file_1.splitlines()
        return economic

    def parse_med(self):
        medicine = self.file_2.splitlines()
        return medicine

    def parse_politice(self):
        politics = self.file_3.splitlines()
        return politics

    def parse_art(self):
        art = self.file_4.splitlines()
        return art

    def parse_IT(self):
        IT = self.file_5.splitlines()
        return IT



