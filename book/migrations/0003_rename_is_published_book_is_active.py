# Generated by Django 5.0.6 on 2024-07-05 05:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0002_alter_publication_phone'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='is_published',
            new_name='is_active',
        ),
    ]
