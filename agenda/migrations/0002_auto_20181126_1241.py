# Generated by Django 2.1.3 on 2018-11-26 14:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='entre',
            name='date',
            field=models.DateTimeField(verbose_name='Data do Evento'),
        ),
        migrations.AlterField(
            model_name='entre',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Descricao do evento'),
        ),
    ]
