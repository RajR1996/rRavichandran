# Generated by Django 2.2 on 2019-04-23 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviewApp', '0006_auto_20190417_1406'),
    ]

    operations = [
        migrations.CreateModel(
            name='Errors',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=50)),
                ('page', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('reportdate', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
