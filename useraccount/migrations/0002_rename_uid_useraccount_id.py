# Generated by Django 5.1.7 on 2025-03-24 15:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('useraccount', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='uid',
            new_name='id',
        ),
    ]
