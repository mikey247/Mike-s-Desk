# Generated by Django 4.0 on 2022-01-23 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_remove_post_image_name_post_image'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UserComment',
        ),
    ]
