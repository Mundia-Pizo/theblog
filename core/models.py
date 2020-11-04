from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField


class Article(models.Model):
    title = models.CharField(max_length=200)
    body = RichTextUploadingField(blank=True, null=True)


    def __str__(self):
        return self.title