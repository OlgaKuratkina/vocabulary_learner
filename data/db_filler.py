from vocabulary.models import Word, Language


def fill_language():
    for lang in ['Esp', 'Eng']:
        Language.create(language=lang)


def fill_from_txt(file_name):
    result = []
    with open(file_name, 'r') as f:
        for line in f.readlines():
            word, type, _ = line.split(',')
            print(word, type)
            record = Word.create(word=word, type=type, language=1)
            result.append(record)
    return result


fill_language()
print(fill_from_txt(file_name='espanol.txt'))
