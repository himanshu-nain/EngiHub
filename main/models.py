from django.db import models
from django.contrib.auth.models import Permission, User


class File(models.Model):

    name = models.CharField(max_length=40)
    size = models.FloatField(default=0)
    author = models.CharField(max_length=40)
    desc = models.CharField(max_length=255)
    dcount = models.IntegerField(default=0)
    lcount = models.IntegerField(default=0)
    dlcount = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploaded_files/')

    def uplike(self):
        self.lcount = self.lcount + 1

    def downlike(self):
        self.dlcount = self.dlcount + 1

    def update(self):
        self.points = self.lcount - self.dlcount
