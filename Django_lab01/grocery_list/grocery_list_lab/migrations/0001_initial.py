# Generated by Django 2.1.7 on 2019-02-28 20:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GroceryItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_description_text', models.CharField(max_length=200)),
                ('created_date', models.DateTimeField(verbose_name='date created')),
                ('completed_date', models.DateTimeField(verbose_name='date completed')),
                ('item_was_completed', models.BooleanField(default=False)),
            ],
        ),
    ]
