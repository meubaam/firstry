# Generated by Django 3.1.5 on 2021-01-31 08:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('fcuser', '0004_fcuser_usereamil'),
    ]

    operations = [
        migrations.RenameField(
            model_name='fcuser',
            old_name='usereamil',
            new_name='useremail',
        ),
    ]
