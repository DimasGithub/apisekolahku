from django.db import models
from datetime import datetime
class Visimisi(models.Model):
    visi = models.TextField()
    misi = models.TextField()

class Pengajarstaff(models.Model):
    nama = models.CharField(max_length = 255)
    nip = models.IntegerField()
    choices_jobs=[
        ('Kepala sekolah', 'Kepala sekolah'),
        ('Wakil kepala sekolah', 'wakil kepala sekolah'),
        ('Kepala staff tata usaha', 'kepala staff tata usaha'),
        ('Pengajar', 'pengajar'),
        ('Staff', 'staff')
    ]
    jobs = models.CharField(max_length = 50, choices=choices_jobs)
    picture = models.ImageField(upload_to='picture/', height_field=None, width_field=None, max_length=100, null=True)


class Pengumuman(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    attachment = models.FileField(upload_to='attachment/', null=True)
    date_created = models.DateTimeField(auto_now_add=True)

class Jadwal(models.Model):
    date_schedule = models.DateField(blank=False)
    tglstr = models.CharField(max_length=25, blank=True)
    events = models.TextField(blank=False)

    def save(self, *args, **kwargs):
        test = datetime.strftime(self.date_schedule,'%Y/%m/%d')
        self.tglstr = test
        super(Jadwal, self).save(*args, **kwargs)

class Pengaturan(models.Model):
    title_bar = models.CharField(max_length = 100)
    title_sub = models.CharField(max_length= 100)
    img_main = models.ImageField(upload_to='picture/', blank=True)
    title_about = models.CharField(max_length= 100)
    content_about = models.CharField(max_length = 2000)
    email_about = models.EmailField()
    phone_about = models.CharField(max_length=20)
    img_about = models.ImageField(upload_to='picture/', blank=True)