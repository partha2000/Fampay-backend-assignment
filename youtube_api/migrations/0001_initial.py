# Generated by Django 3.2 on 2021-04-17 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='testModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='videoData',
            fields=[
                ('videoID', models.CharField(default=1, editable=False, max_length=50, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('channel_name', models.CharField(max_length=20)),
                ('pub_date_time', models.DateTimeField()),
                ('thumbnailURL', models.URLField()),
            ],
        ),
    ]