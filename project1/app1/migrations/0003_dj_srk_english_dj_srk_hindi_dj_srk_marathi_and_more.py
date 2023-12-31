# Generated by Django 4.2.6 on 2023-10-26 08:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_dj_srk_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='dj_srk',
            name='English',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dj_srk',
            name='Hindi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dj_srk',
            name='Marathi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='dj_srk',
            name='city',
            field=models.CharField(default=False, max_length=100),
        ),
        migrations.AddField(
            model_name='dj_srk',
            name='gender',
            field=models.CharField(default=False, max_length=20),
        ),
        migrations.AddField(
            model_name='dj_srk',
            name='time',
            field=models.TimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
