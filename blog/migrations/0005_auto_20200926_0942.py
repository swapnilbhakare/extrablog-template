# Generated by Django 3.0.6 on 2020-09-26 04:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200924_1427'),
    ]

    operations = [
        migrations.RenameField(
            model_name='extrabloghome',
            old_name='comments',
            new_name='commentCount',
        ),
    ]