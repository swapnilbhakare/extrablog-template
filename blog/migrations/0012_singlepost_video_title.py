# Generated by Django 3.0.6 on 2020-09-26 09:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20200926_1449'),
    ]

    operations = [
        migrations.AddField(
            model_name='singlepost',
            name='video_title',
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
    ]