from django.contrib import admin
from visimisi.models import Visimisi, Jadwal, Pengaturan

admin.site.register(Visimisi)
# Register your models here.
admin.site.register(Jadwal)
admin.site.register(Pengaturan)