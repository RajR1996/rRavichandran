# Generated by Django 2.2 on 2019-04-16 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20190416_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profilephoto',
            field=models.ImageField(default='default_profile.jpg', upload_to='profiles'),
        ),
    ]
