# Generated by Django 3.2.6 on 2021-08-21 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('provider', '0002_auto_20210821_2341'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='provider',
            name='user',
        ),
        migrations.AddField(
            model_name='provider',
            name='email',
            field=models.EmailField(default='default@mail.com', max_length=50),
        ),
        migrations.AddField(
            model_name='provider',
            name='name',
            field=models.CharField(default='name', max_length=50),
        ),
    ]