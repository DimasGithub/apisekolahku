# Generated by Django 3.2 on 2021-05-03 08:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('visimisi', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pengajarstaff',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nama', models.CharField(max_length=255)),
                ('nip', models.IntegerField()),
                ('jobs', models.CharField(choices=[('Kepala sekolah', 'kepala sekolah'), ('Wakil kepala sekolah', 'wakil kepala sekolah'), ('Kepala staff tata usaha', 'kepala staff tata usaha'), ('Pengajar', 'pengajar'), ('Staff', 'staff')], max_length=50)),
                ('picture', models.ImageField(upload_to='picture/')),
            ],
        ),
    ]
