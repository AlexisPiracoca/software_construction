# Generated by Django 3.2.7 on 2021-11-01 01:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('characters', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='character',
            old_name='cit',
            new_name='cit_id',
        ),
        migrations.RenameField(
            model_name='character',
            old_name='uni',
            new_name='uni_id',
        ),
        migrations.RenameField(
            model_name='powercharacter',
            old_name='cha',
            new_name='cha_id',
        ),
        migrations.RenameField(
            model_name='powercharacter',
            old_name='pow',
            new_name='pow_id',
        ),
    ]