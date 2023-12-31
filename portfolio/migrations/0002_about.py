# Generated by Django 4.2.3 on 2023-09-04 10:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profile_pic', models.ImageField(upload_to='about/')),
                ('name', models.CharField(max_length=100)),
                ('designation', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=100, unique=True)),
                ('phone_number', models.CharField(max_length=16, unique=True)),
            ],
            options={
                'verbose_name': 'about',
                'verbose_name_plural': 'abouts',
                'db_table': '',
                'managed': True,
            },
        ),
    ]
