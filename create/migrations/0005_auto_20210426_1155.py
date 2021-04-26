# Generated by Django 3.2 on 2021-04-26 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('create', '0004_alter_login_options'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='login',
            name='email',
        ),
        migrations.RemoveField(
            model_name='login',
            name='password01',
        ),
        migrations.RemoveField(
            model_name='login',
            name='password02',
        ),
        migrations.RemoveField(
            model_name='login',
            name='phone',
        ),
        migrations.AddField(
            model_name='login',
            name='about',
            field=models.TextField(default='', max_length=500),
        ),
    ]