# Generated by Django 3.1.6 on 2021-02-16 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cinema',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),  # NOQA
                ('name', models.CharField(max_length=100)),
                ('location', models.CharField(max_length=200, null=True)),
                ('description', models.CharField(max_length=400, null=True)),
            ],
        ),
    ]
