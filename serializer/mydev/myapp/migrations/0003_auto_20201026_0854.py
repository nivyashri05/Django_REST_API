# Generated by Django 3.1.2 on 2020-10-26 08:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_auto_20201026_0818'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collegetb',
            old_name='dpthod',
            new_name='depthod',
        ),
    ]