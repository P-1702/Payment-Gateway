# Generated by Django 3.1.7 on 2021-08-03 04:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20210803_0949'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Payments',
            new_name='Payment',
        ),
    ]