# Generated by Django 3.2 on 2021-05-08 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visimisi', '0004_pengumuman'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pengumuman',
            name='attachment',
            field=models.FileField(null=True, upload_to='attachment/'),
        ),
    ]
