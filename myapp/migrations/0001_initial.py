# Generated by Django 5.0.1 on 2024-01-17 08:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='producttable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('price', models.FloatField()),
                ('description', models.TextField()),
                ('proimage', models.ImageField(upload_to='photos')),
            ],
        ),
    ]
