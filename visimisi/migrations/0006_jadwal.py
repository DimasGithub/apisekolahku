# Generated by Django 3.2 on 2021-05-17 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visimisi', '0005_alter_pengumuman_attachment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Jadwal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_schedule', models.DateField()),
                ('events', models.TextField()),
            ],
        ),
    ]
