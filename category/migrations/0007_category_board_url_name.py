# Generated by Django 3.0.6 on 2020-09-11 05:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0006_auto_20200618_1546'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='board_url_name',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]
