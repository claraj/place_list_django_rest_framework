# Generated by Django 4.0.2 on 2022-02-21 23:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapi', '0010_rename_datecreated_place_dateadded'),
    ]

    operations = [
        migrations.RenameField(
            model_name='place',
            old_name='isStarred',
            new_name='starred',
        ),
    ]
