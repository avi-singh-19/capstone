# Generated by Django 4.2.2 on 2023-12-16 17:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='stock',
            name='date_searched',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
