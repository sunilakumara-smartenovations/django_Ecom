# Generated by Django 2.2.3 on 2022-01-12 17:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('phone_no', models.IntegerField()),
                ('email_ID', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
    ]
