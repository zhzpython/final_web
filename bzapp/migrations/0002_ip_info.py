# Generated by Django 2.0.6 on 2019-07-06 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bzapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ip_info',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, null=True)),
                ('apply_time', models.FloatField()),
                ('flag', models.CharField(max_length=10, null=True)),
                ('forbid_time', models.FloatField()),
            ],
        ),
    ]
