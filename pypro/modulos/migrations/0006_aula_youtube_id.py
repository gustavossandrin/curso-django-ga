# Generated by Django 4.0.2 on 2022-02-17 16:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('modulos', '0005_aula'),
    ]

    operations = [
        migrations.AddField(
            model_name='aula',
            name='youtube_id',
            field=models.CharField(default='1', max_length=32),
        ),
    ]
