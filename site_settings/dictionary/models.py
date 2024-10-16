from django.db import models
from django.db.models import Model


class Word(models.Model):
    id = models.AutoField(primary_key=True)
    word = models.CharField(max_length=255)
    translation = models.CharField(max_length=500)
    topic = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.word}/{self.translation}/{str(self.topic)}"

    class Meta:
        db_table = 'words'
        managed = False
