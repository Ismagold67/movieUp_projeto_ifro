# Generated by Django 5.0.6 on 2024-09-17 20:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_filme_situacao'),
    ]

    operations = [
        migrations.RenameField(
            model_name='filme',
            old_name='ano_lancamento',
            new_name='data_lancamento',
        ),
    ]
