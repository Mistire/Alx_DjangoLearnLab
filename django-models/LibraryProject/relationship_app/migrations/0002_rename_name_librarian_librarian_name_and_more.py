# Generated by Django 5.2.4 on 2025-07-15 08:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('relationship_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='librarian',
            old_name='name',
            new_name='librarian_name',
        ),
        migrations.RenameField(
            model_name='library',
            old_name='name',
            new_name='library_name',
        ),
    ]
