from bson import ObjectId
from django.db.models import permalink

from django_mongoengine import Document
from django_mongoengine import fields


class Artist(Document):
    id = fields.StringField(primary_key=True, default=ObjectId)
    name = fields.StringField(max_length=100)

    class Meta:
        ordering = ['name'],
        verbose_name = 'professional artist',
        verbose_name_plural = 'professional artists'

    def __unicode__(self):
        return self.name

    @permalink
    def get_absolute_url(self):
        return ('artist_detail', (), {'pk': self.id})


class Author(Document):
    id = fields.StringField(primary_key=True, default=ObjectId)
    name = fields.StringField(max_length=100)
    slug = fields.StringField()

    _meta = {
        "ordering": ['name'],
        "exclude": 'id'
    }

    def __unicode__(self):
        return self.name


class Book(Document):
    id = fields.StringField(primary_key=True, default=ObjectId)
    name = fields.StringField(max_length=300)
    slug = fields.StringField()
    pages = fields.IntField()
    authors = fields.ListField(fields.ReferenceField(Author))
    pubdate = fields.DateTimeField()

    _meta = {
        "ordering": ['-pubdate']
    }

    def __unicode__(self):
        return self.name


class Page(Document):
    id = fields.StringField(primary_key=True, default=ObjectId)
    content = fields.StringField()
    template = fields.StringField(max_length=300)
