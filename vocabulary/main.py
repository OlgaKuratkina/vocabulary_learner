from data import db_filler

from vocabulary import db
from vocabulary.settings import FILE_NAME
from vocabulary.models import Language, Word, Translation


db.create_tables([Language, Word, Translation])
db_filler.fill_language()
db_filler.fill_from_txt(FILE_NAME)
