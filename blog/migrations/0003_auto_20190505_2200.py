# Generated by Django 2.0.2 on 2019-05-05 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20190505_2159'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='pub_date',
            field=models.DateTimeField(),
        ),
    ]
