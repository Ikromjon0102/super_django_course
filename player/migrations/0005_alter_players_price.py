# Generated by Django 4.2.5 on 2023-09-12 05:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('player', '0004_alter_players_height'),
    ]

    operations = [
        migrations.AlterField(
            model_name='players',
            name='price',
            field=models.CharField(blank=True, max_length=100),
        ),
    ]
