# Generated by Django 5.0.5 on 2024-06-03 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_create_data_post_created_data_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to='intruder_image/%Y/%m%d/'),
            preserve_default=False,
        ),
    ]
