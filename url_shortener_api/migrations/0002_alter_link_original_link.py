# Generated by Django 4.0.6 on 2022-07-13 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_api', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='original_link',
            field=models.URLField(max_length=250),
        ),
    ]
