# Generated by Django 2.2.3 on 2022-01-19 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travello', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slide01',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttl1', models.CharField(max_length=10)),
                ('ttl2', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='slide01/pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='slide02',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ttl1', models.CharField(max_length=10)),
                ('ttl2', models.CharField(max_length=10)),
                ('img', models.ImageField(upload_to='slide02/pics')),
                ('desc', models.TextField()),
            ],
        ),
        migrations.RemoveField(
            model_name='product',
            name='offer_price',
        ),
    ]
