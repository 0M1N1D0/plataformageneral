# Generated by Django 4.2.1 on 2023-05-12 22:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('examen', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='respuestausuario',
            options={'ordering': ['respuesta_usuario'], 'verbose_name': 'Respuesta del agente', 'verbose_name_plural': 'Respuestas del agente'},
        ),
        migrations.AddField(
            model_name='respuestausuario',
            name='respuesta_correcta',
            field=models.BooleanField(default=False, verbose_name='¿Es correcta?'),
        ),
    ]