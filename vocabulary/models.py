import peewee

from vocabulary import db


class BaseModel(peewee.Model):
    class Meta:
        database = db


class Language(BaseModel):
    language_name = peewee.CharField


class Word(BaseModel):
    word = peewee.CharField()
    type = peewee.CharField(null=True)
    language = peewee.ForeignKeyField(Language)


class Translation(BaseModel):
    origin_word = peewee.ForeignKeyField(Word)
    translated_word = peewee.ForeignKeyField(Word)
    translation_rank = peewee.IntegerField(choices=(1, 2, 3), default=1)


