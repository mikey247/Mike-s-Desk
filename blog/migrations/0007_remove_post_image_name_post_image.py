# Generated by Django 4.0 on 2022-01-23 13:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_post_comments_remove_usercomment_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='Image_name',
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(null=True, upload_to='posts'),
        ),
    ]
