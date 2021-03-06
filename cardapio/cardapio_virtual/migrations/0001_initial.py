# Generated by Django 3.2.6 on 2021-11-18 01:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=30)),
                ('descricao', models.CharField(max_length=200)),
                ('imagem', models.CharField(max_length=512)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=9)),
            ],
            options={
                'db_table': 'itens',
            },
        ),
    ]
