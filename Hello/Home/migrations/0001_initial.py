# Generated by Django 5.0.2 on 2024-05-12 04:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=50)),
                ('Number', models.IntegerField(max_length=50)),
                ('Email', models.EmailField(max_length=254)),
                ('Password', models.CharField(max_length=50)),
            ],
        ),
    ]
