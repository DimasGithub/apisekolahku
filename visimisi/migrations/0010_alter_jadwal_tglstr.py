# Generated by Django 3.2 on 2021-05-19 01:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visimisi', '0009_jadwal_tglstr'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='tglstr',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]