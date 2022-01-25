# Generated by Django 3.0.3 on 2020-04-10 13:30

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0005_auto_20200410_1322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='about',
            options={'verbose_name_plural': 'About'},
        ),
        migrations.AlterModelOptions(
            name='family',
            options={'verbose_name_plural': 'Families'},
        ),
        migrations.AddField(
            model_name='services',
            name='Venue',
            field=models.CharField(blank=True, max_length=50),
        ),
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 853574, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 849670, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 850646, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 855526, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 853574, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 849670, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='services',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 851622, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 13, 29, 57, 852598, tzinfo=utc), verbose_name='date published'),
        ),
    ]
