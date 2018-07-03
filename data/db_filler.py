from vocabulary import db
from vocabulary.models import Word, Language


def fill_language():
    for lang in ['Esp', 'Eng']:
        Language.create(language=lang)


def fill_from_txt(file_name):
    data = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            word, type, _ = line.split(',')
            data.append((word.strip(), type.strip(), 1))

    with db.atomic():
        Word.insert_many(data, fields=[Word.word, Word.type, Word.language]).execute()
    return data
