# Generated by Django 2.1.7 on 2019-02-28 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('grocery_list_lab', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groceryitem',
            name='completed_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]