# Generated by Django 4.2.7 on 2024-01-23 01:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_urlmodel_name_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='project_url',
            field=models.CharField(default=django.utils.timezone.now, max_length=300, verbose_name='proje url'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='project',
            name='project_url_name',
            field=models.CharField(default=django.utils.timezone.now, max_length=200, verbose_name='proje url adi'),
            preserve_default=False,
        ),
    ]
