# Generated by Django 2.2 on 2019-04-13 23:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('brand', models.CharField(max_length=100)),
                ('cost', models.DecimalField(decimal_places=2, default=0.0, max_digits=8)),
                ('category', models.CharField(max_length=100)),
                ('releasedate', models.DateField()),
                ('description', models.TextField()),
                ('productphoto', models.ImageField(default='default_product.jpg', upload_to='reviewApp/static/product_images')),
            ],
        ),
    ]
