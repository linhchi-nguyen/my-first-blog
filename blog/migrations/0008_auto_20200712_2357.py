# Generated by Django 2.2.12 on 2020-07-12 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200712_1837'),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='complete',
            new_name='done',
        ),
        migrations.RenameField(
            model_name='task',
            old_name='title',
            new_name='todo',
        ),
    ]
