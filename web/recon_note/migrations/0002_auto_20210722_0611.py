# Generated by Django 3.2.4 on 2021-07-22 06:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recon_note', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='todonote',
            name='is_done',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todonote',
            name='is_important',
            field=models.BooleanField(default=False),
        ),
    ]