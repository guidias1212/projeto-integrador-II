# Generated by Django 3.2.6 on 2022-06-28 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cardapio_virtual', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='item',
            name='curtidas',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
    ]
