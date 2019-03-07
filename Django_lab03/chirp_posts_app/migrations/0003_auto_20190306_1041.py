# Generated by Django 2.1.7 on 2019-03-06 18:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chirp_posts_app', '0002_post_chirp_title'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='chirp_author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='post',
            name='chirp_title',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
