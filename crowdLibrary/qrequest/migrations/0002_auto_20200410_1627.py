# Generated by Django 2.2.2 on 2020-04-10 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qrequest', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='book',
            name='name',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
