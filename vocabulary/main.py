import peewee

from vocabulary import db
from vocabulary.models import Language, Word, Translation


db.create_tables([Language, Word, Translation])
