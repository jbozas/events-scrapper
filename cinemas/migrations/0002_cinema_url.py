# Generated by Django 3.1.6 on 2021-02-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cinemas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='cinema',
            name='url',
            field=models.CharField(max_length=400, null=True),
        ),
    ]
