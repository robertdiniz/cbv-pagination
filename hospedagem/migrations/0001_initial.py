# Generated by Django 4.2.2 on 2023-11-23 18:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55, verbose_name='Nome cliente')),
                ('email', models.EmailField(max_length=254, verbose_name='Email')),
                ('telefone', models.CharField(max_length=15, verbose_name='Telefone')),
                ('endereco', models.TextField(verbose_name='Endereço')),
            ],
        ),
        migrations.CreateModel(
            name='Quarto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apartamento', models.IntegerField(verbose_name='Apartamento')),
                ('valor', models.FloatField(verbose_name='Valor')),
            ],
        ),
        migrations.CreateModel(
            name='Hospedagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_entrada', models.DateField(verbose_name='Data entrada')),
                ('data_saida', models.DateField(verbose_name='Data saída')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospedagem.cliente')),
                ('quarto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospedagem.quarto')),
            ],
        ),
        migrations.CreateModel(
            name='Consumo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=55, verbose_name='Nome consumo')),
                ('data', models.DateField(verbose_name='Data')),
                ('valor', models.FloatField(verbose_name='Valor')),
                ('hospedagem', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='hospedagem.hospedagem')),
            ],
        ),
    ]