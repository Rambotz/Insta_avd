# Generated by Django 3.2.3 on 2023-03-21 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('twbot', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='useravd',
            name='twitter_account',
        ),
        migrations.DeleteModel(
            name='TwitterActionLog',
        ),
    ]
