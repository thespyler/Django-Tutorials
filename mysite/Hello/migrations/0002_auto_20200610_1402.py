# Generated by Django 3.0.6 on 2020-06-10 08:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Hello', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Fruit',
            new_name='Student',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='num',
            new_name='roll_no',
        ),
    ]