# Generated by Django 4.2.11 on 2024-04-29 14:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('invista_me', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='investimento',
            old_name='investimetno',
            new_name='investimento',
        ),
    ]