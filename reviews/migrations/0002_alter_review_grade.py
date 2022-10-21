from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reviews', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='review',
            name='grade',

            field=models.IntegerField(choices=[(4, '★★★★'), (3, '★★★'), (1, '★'), (5, '★★★★★'), (2, '★★')], default=None),

        ),
    ]
