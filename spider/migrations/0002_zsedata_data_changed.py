# Generated by Django 3.2.3 on 2021-06-12 20:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('spider', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='zsedata',
            name='data_changed',
            field=models.BooleanField(default=False),
        ),
    ]