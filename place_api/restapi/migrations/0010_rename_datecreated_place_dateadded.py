# Generated by Django 4.0.2 on 2022-02-21 20:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0009_remove_place_priority_place_datecreated_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='dateCreated',
            new_name='dateAdded',
        ),
    ]
