# Generated by Django 5.1.4 on 2025-01-14 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Books',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
                ('author', models.CharField(max_length=20)),
                ('price', models.IntegerField()),
                ('language', models.CharField(max_length=20)),
                ('pages', models.IntegerField()),
                ('image', models.ImageField(upload_to='images')),
                ('pdf', models.FileField(upload_to='files')),
            ],
        ),
    ]
