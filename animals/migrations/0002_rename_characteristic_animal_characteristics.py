# Generated by Django 4.0.5 on 2022-07-05 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('animals', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='animal',
            old_name='characteristic',
            new_name='characteristics',
        ),
    ]
