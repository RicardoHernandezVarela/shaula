# Generated by Django 2.0.8 on 2019-01-23 23:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0018_auto_20190123_1714'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='actividad',
            options={'ordering': ['fecha']},
        ),
        migrations.AlterField(
            model_name='actividad',
            name='categoria',
            field=models.CharField(choices=[('tarea', 'Tarea'), ('ejclase', 'Ejercicios clase'), ('examen', 'Examen'), ('practica', 'Práctica'), ('extra', 'Extra'), ('proyecto', 'Proyecto')], max_length=50),
        ),
    ]