# Generated by Django 4.0.4 on 2022-05-25 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0017_tfc_remove_achivement_competencias_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=60)),
                ('pergunta_1', models.CharField(max_length=20)),
                ('pergunta_2', models.CharField(max_length=20)),
                ('pergunta_3', models.CharField(max_length=10)),
            ],
        ),
    ]
