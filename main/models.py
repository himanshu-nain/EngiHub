from django.db import models
import os
from django.conf import settings
from django.contrib.auth.models import Permission, User


class File(models.Model):

    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    desc = models.CharField(max_length=255)
    dcount = models.IntegerField(default=0)
    lcount = models.IntegerField(default=0)
    dlcount = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploaded_files/')
    size = models.FloatField(default=0.0)


    def uplike(self):
        self.lcount = self.lcount + 1

    def downlike(self):
        self.dlcount = self.dlcount + 1

    def update(self):
        self.points = self.lcount - self.dlcount

    def delete(self, *args, **kwargs):
        os.remove(os.path.join(settings.MEDIA_ROOT.join('uploaded_files'), self.file.name))
        super(File, self).delete(*args, **kwargs)