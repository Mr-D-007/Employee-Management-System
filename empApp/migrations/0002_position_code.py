# Generated by Django 3.2.4 on 2021-09-05 09:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('empApp', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='position',
            name='code',
            field=models.CharField(default=101, max_length=5),
            preserve_default=False,
        ),
    ]