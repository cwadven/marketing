# Generated by Django 3.0.6 on 2020-06-05 08:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_commentalert'),
        ('usingform', '0014_auto_20200604_2336'),
    ]

    operations = [
        migrations.CreateModel(
            name='Commentalertcontent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(max_length=300)),
                ('board', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usingform.Defaultform')),
                ('profile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='account.Profile')),
            ],
        ),
    ]
