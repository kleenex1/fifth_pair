# Generated by Django 3.2.13 on 2022-10-21 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='grade',
            field=models.IntegerField(choices=[(3, '★★★'), (2, '★★'), (4, '★★★★'), (1, '★'), (5, '★★★★★')], default=None),
        ),
    ]
