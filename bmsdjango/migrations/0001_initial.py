# Generated by Django 3.0.2 on 2022-03-28 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('isbn', models.CharField(max_length=128, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
