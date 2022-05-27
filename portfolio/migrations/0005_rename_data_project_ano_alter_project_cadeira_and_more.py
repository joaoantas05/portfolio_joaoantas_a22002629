# Generated by Django 4.0.4 on 2022-05-19 13:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_alter_project_data'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='data',
            new_name='ano',
        ),
        migrations.AlterField(
            model_name='project',
            name='cadeira',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='project',
            name='imagem',
            field=models.ImageField(upload_to='static/portfolio/images'),
        ),
    ]
