# Generated by Django 3.0.3 on 2020-04-14 05:45

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0009_auto_20200414_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='sermons',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 595735, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 599724, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 596732, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='department',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 595735, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 597730, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 601719, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 600721, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 596732, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='services',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 598727, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 14, 5, 45, 29, 599724, tzinfo=utc), verbose_name='date published'),
        ),
    ]
