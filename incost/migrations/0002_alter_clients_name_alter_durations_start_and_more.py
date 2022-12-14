# Generated by Django 4.0.6 on 2022-07-26 10:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('incost', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clients',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='durations',
            name='start',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='durations',
            name='stop',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='equipment',
            name='name',
            field=models.TextField(max_length=100),
        ),
        migrations.AlterField(
            model_name='modes',
            name='name',
            field=models.TextField(max_length=100),
        ),
    ]
