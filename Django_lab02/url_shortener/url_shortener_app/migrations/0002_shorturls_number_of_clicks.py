# Generated by Django 2.1.7 on 2019-03-02 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('url_shortener_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='shorturls',
            name='number_of_clicks',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
