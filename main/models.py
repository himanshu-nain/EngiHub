from django.db import models
from django.contrib.auth.models import Permission, User
from django.utils import timezone


class File(models.Model):

    name = models.CharField(max_length=40)
    author = models.CharField(max_length=40)
    desc = models.CharField(max_length=255, blank=True)
    dcount = models.IntegerField(default=0)
    lcount = models.IntegerField(default=0)
    dlcount = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    file = models.FileField(upload_to='uploaded_files/')
    size = models.FloatField(default=0.0, )
    size_postfix = models.CharField(blank=True, max_length=2)
    upload_time = models.DateField(default=timezone.now)
    uploader = models.ForeignKey(User, blank=True, on_delete=models.CASCADE)

    def clean(self):

        temp = self.file.size / 1048576

        if temp < 1:
            self.size = float("{0:.2f}".format(temp * 1024))
            self.size_postfix = 'KB'
        else:
            self.size = float("{0:.2f}".format(temp))
            self.size_postfix = 'MB'

    def uplike(self):
        self.lcount = self.lcount + 1

    def downlike(self):
        self.dlcount = self.dlcount + 1

    def update(self):
        self.points = self.lcount - self.dlcount

    # def delete(self, *args, **kwargs):
    #    os.remove(os.path.join(settings.MEDIA_ROOT, self.file))
    #    super(File, self).delete(*args, **kwargs)