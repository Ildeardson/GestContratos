# Generated by Django 3.2.4 on 2021-06-17 19:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fornecedores', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fornecedores',
            name='telefone',
            field=models.CharField(default='', max_length=11, verbose_name='Telfone'),
            preserve_default=False,
        ),
    ]
