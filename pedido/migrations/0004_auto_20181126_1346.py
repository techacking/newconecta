# Generated by Django 2.1.3 on 2018-11-26 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cadastro', '0003_auto_20181126_1346'),
        ('pedido', '0003_auto_20181126_0209'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tabelapreco',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipovalor', models.CharField(max_length=40)),
                ('valor', models.DecimalField(decimal_places=2, default=0, max_digits=8)),
                ('sala', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cadastro.Sala')),
            ],
        ),
        migrations.AlterField(
            model_name='orcamento',
            name='dataevento',
            field=models.DateTimeField(verbose_name='Data para Orcamento'),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='valor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='pedido.Tabelapreco'),
        ),
    ]