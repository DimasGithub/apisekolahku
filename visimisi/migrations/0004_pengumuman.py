# Generated by Django 3.2 on 2021-05-07 18:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visimisi', '0003_auto_20210506_0218'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengumuman',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('attachment', models.FileField(upload_to='attachment/')),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
