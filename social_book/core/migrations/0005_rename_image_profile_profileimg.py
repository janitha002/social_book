# Generated by Django 5.0.6 on 2024-06-24 12:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_profile_id_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='image',
            new_name='profileimg',
        ),
    ]
