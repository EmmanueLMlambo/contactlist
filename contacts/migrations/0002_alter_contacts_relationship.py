# Generated by Django 4.1.5 on 2023-02-15 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='relationship',
            field=models.CharField(max_length=50),
        ),
    ]
