# Generated by Django 3.2 on 2021-05-18 18:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visimisi', '0006_jadwal'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jadwal',
            name='events',
            field=models.TextField(default='2021/05/19'),
        ),
    ]
