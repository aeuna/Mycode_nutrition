# Generated by Django 3.0.6 on 2020-07-31 10:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('foodApp', '0005_auto_20200728_1633'),
    ]

    operations = [
        migrations.RenameField(
            model_name='ingredient',
            old_name='caffein',
            new_name='Cholesterol',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='calcium',
            new_name='calorie',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='carlorie',
            new_name='protein',
        ),
        migrations.RenameField(
            model_name='ingredient',
            old_name='salt',
            new_name='sodium',
        ),
    ]
