# Generated by Django 3.1.3 on 2020-11-19 16:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20201106_2327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calculate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mname', models.CharField(max_length=100)),
                ('mgenre', models.CharField(max_length=200)),
                ('mreview', models.TextField()),
                ('mscore', models.IntegerField()),
            ],
        ),
    ]
