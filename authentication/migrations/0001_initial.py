# Generated by Django 5.0 on 2023-12-14 04:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.CharField(max_length=60, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=60)),
                ('email', models.EmailField(max_length=254)),
                ('psw', models.CharField(max_length=50)),
                ('_date', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
