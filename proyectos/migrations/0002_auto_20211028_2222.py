# Generated by Django 3.2.5 on 2021-10-29 01:22

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='detalle',
            field=models.TextField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='app_url',
            field=models.URLField(blank=True, null=True, verbose_name='link_app'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='github_url',
            field=models.URLField(blank=True, null=True, verbose_name='link_github'),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='nombre',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
