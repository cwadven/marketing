# Generated by Django 3.0.6 on 2020-09-11 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0007_category_board_url_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='board_url_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
