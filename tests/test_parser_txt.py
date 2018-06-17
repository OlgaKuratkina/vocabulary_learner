import pytest

from vocabulary.parser_txt import Parser


def test_parse_words():
    raw_string = "reclamo m 1) реклама 2) подсадная\nптица; приманка 3) юр иск 4) юр\nпротест"
    parser = Parser(raw_string)
    out = parser.parse()
    assert out['origin_word'] == 'reclamo'
    assert out['translation'] == ['реклама', 'подсадная птица', 'приманка', 'юр иск', 'юр протест']