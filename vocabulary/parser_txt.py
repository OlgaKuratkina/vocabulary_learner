import re


class Parser:
    """reclamo m 1) реклама 2) подсадная\nптица; приманка 3) юр иск 4) юр\nпротест"""
    def __init__(self, raw_string):
        self.raw_string = raw_string

    def parse(self):
        out = {}
        text = self.raw_string.replace('\n', ' ')
        out['origin_word'] = text.split()[0]
        out['translation'] = []
        m = re.findall(r'(?<=\\d)\w+', text)
        # out['translation'] = m.group(0)
        print(m)
        # r'(?<=\[1-5]\)) \w+'
        return out
