# Generated by Django 4.0.4 on 2022-05-24 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0012_alter_project_ano'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='tecnologia',
            field=models.ManyToManyField(to='portfolio.tecnologia'),
        ),
    ]
