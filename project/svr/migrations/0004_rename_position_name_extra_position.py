# Generated by Django 4.1.4 on 2022-12-16 16:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('svr', '0003_rename_position_extra_position_name_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extra',
            old_name='position_name',
            new_name='position',
        ),
    ]
