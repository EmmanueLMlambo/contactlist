# Generated by Django 4.1.5 on 2023-02-23 11:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0004_alter_contacts_department_alter_contacts_full_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contacts',
            name='department',
            field=models.CharField(max_length=50),
        ),
    ]
