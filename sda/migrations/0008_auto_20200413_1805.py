# Generated by Django 3.0.3 on 2020-04-13 15:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('sda', '0007_auto_20200410_1702'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sermons',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sermon_title', models.CharField(max_length=20)),
                ('sermon_speaker', models.CharField(max_length=30)),
                ('sermon_link', models.CharField(max_length=50)),
            ],
        ),
        migrations.AddField(
            model_name='church_member',
            name='is_leader',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='about',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 483855, tzinfo=utc), verbose_name='date published'),
        ),
        migrations.AlterField(
            model_name='announcement',
            name='publication_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 478974, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='event',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 480926, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='faq',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 486782, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='otherbussiness',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 484831, tzinfo=utc), verbose_name='Date Published'),
        ),
        migrations.AlterField(
            model_name='scripture',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 479950, tzinfo=utc), verbose_name='Date published'),
        ),
        migrations.AlterField(
            model_name='services',
            name='TimeLIne',
            field=models.CharField(blank=True, choices=[('Morning', 'Morning'), ('Afternoon', 'Afternoon'), ('Evening', 'Evening')], max_length=50),
        ),
        migrations.AlterField(
            model_name='services',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 480926, tzinfo=utc), verbose_name='Publication Date'),
        ),
        migrations.AlterField(
            model_name='visitor_word',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 4, 13, 15, 5, 16, 482879, tzinfo=utc), verbose_name='date published'),
        ),
    ]