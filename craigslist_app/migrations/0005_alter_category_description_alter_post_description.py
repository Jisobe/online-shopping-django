# Generated by Django 4.0.3 on 2022-04-04 07:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('craigslist_app', '0004_alter_post_price_alter_post_price_currency'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='description',
            field=models.TextField(max_length=500),
        ),
        migrations.AlterField(
            model_name='post',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]
