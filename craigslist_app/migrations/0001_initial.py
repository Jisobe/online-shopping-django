# Generated by Django 4.0.3 on 2022-04-03 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=255)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('contact_info', models.CharField(max_length=255)),
                ('picture', models.ImageField(upload_to=None)),
                ('post_date', models.DateField(auto_now_add=True)),
                ('last_activity', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(related_name='posts', to='craigslist_app.category')),
            ],
        ),
    ]
