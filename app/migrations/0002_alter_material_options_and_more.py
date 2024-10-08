# Generated by Django 5.1.1 on 2024-09-16 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='material',
            options={'verbose_name': 'Material', 'verbose_name_plural': 'Materiais'},
        ),
        migrations.AlterModelOptions(
            name='material_adicionado',
            options={'verbose_name': 'Material Adicionado', 'verbose_name_plural': 'Materiais Adicionados'},
        ),
        migrations.AlterModelOptions(
            name='ocupacao',
            options={'verbose_name': 'Ocupação', 'verbose_name_plural': 'Ocupações'},
        ),
        migrations.AlterModelOptions(
            name='perguntas',
            options={'verbose_name': 'Perguntas', 'verbose_name_plural': 'Perguntas'},
        ),
        migrations.AlterModelOptions(
            name='questionario',
            options={'verbose_name': 'Questionário', 'verbose_name_plural': 'Questionários'},
        ),
        migrations.AlterModelOptions(
            name='usuario',
            options={'verbose_name': 'Usuário', 'verbose_name_plural': 'Usuários'},
        ),
        migrations.AlterField(
            model_name='material',
            name='administrador',
            field=models.CharField(max_length=100, verbose_name='Administrador do material'),
        ),
        migrations.AlterField(
            model_name='material',
            name='conteudo',
            field=models.CharField(max_length=100000, verbose_name='Conteúdo do material'),
        ),
        migrations.AlterField(
            model_name='material',
            name='nome',
            field=models.CharField(max_length=100, verbose_name='Nome do material'),
        ),
    ]
