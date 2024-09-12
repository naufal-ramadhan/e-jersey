# Generated by Django 5.1.1 on 2024-09-12 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
                ('description', models.TextField()),
                ('type', models.CharField(max_length=255)),
                ('club', models.CharField(max_length=255)),
                ('slug', models.SlugField(blank=True, unique=True)),
            ],
        ),
    ]
