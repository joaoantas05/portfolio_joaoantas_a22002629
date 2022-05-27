# Generated by Django 4.0.4 on 2022-05-23 21:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_alter_new_autor_alter_noticia_titulo_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='chair',
            name='topicosabordados',
        ),
        migrations.RemoveField(
            model_name='person',
            name='link',
        ),
        migrations.AddField(
            model_name='chair',
            name='ano_letivo',
            field=models.CharField(default='1', max_length=20),
        ),
        migrations.AddField(
            model_name='chair',
            name='docente_teorica',
            field=models.ForeignKey(default='1', on_delete=django.db.models.deletion.CASCADE, to='portfolio.person'),
        ),
        migrations.AddField(
            model_name='chair',
            name='docentes_praticas',
            field=models.ManyToManyField(related_name='professor_pratica', to='portfolio.person'),
        ),
        migrations.AddField(
            model_name='chair',
            name='linguagens',
            field=models.ManyToManyField(blank=True, to='portfolio.tecnologia'),
        ),
        migrations.AddField(
            model_name='chair',
            name='link_cadeira',
            field=models.CharField(default='1', max_length=1000),
        ),
        migrations.AddField(
            model_name='chair',
            name='projetos',
            field=models.ManyToManyField(blank=True, to='portfolio.project'),
        ),
        migrations.AddField(
            model_name='chair',
            name='topicos_abordados',
            field=models.CharField(default='1', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='linklinkedin',
            field=models.CharField(default='1', max_length=1000),
        ),
        migrations.AddField(
            model_name='person',
            name='linklusofona',
            field=models.CharField(default='1', max_length=1000),
        ),
        migrations.AlterField(
            model_name='chair',
            name='nome',
            field=models.CharField(max_length=60),
        ),
    ]
