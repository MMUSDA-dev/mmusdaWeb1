# Generated by Django 3.0.3 on 2020-04-10 09:56

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0003_auto_20200410_1240'),
    ]

    operations = [
        migrations.RenameField(
            model_name='services',
            old_name='time',
            new_name='Time_From',
        ),
        migrations.AddField(
            model_name='services',
            name='Time_To',
            field=models.TimeField(blank=True, default=datetime.datetime(2020, 4, 10, 9, 56, 12, 545498, tzinfo=utc)),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 438198, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 435205, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 436202, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 440191, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 438198, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 435205, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='services',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 436202, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 10, 9, 55, 55, 437199, tzinfo=utc), verbose_name='date published'),
        ),
    ]