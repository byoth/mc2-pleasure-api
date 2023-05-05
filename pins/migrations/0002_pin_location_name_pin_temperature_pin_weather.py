# Generated by Django 4.2 on 2023-05-05 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pins', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='pin',
            name='location_name',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='pin',
            name='temperature',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='pin',
            name='weather',
            field=models.CharField(choices=[('sunny', 'Sunny'), ('cloudy', 'Cloudy'), ('rainy', 'Rainy'), ('snowy', 'Snowy')], max_length=20, null=True),
        ),
    ]
