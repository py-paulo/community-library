# Generated by Django 3.1.5 on 2021-01-22 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_auto_20210121_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='display_cover',
            field=models.BooleanField(blank=True, default=False, null=True, verbose_name='Exibir foto'),
        ),
    ]
