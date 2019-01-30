# Generated by Django 2.0.8 on 2019-01-23 23:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0016_auto_20190121_2259'),
    ]

    operations = [
        migrations.CreateModel(
            name='Calificacion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puntos', models.FloatField()),
            ],
        ),
        migrations.AlterField(
            model_name='actividad',
            name='categoria',
            field=models.CharField(choices=[('extra', 'Extra'), ('proyecto', 'Proyecto'), ('ejclase', 'Ejercicios clase'), ('examen', 'Examen'), ('tarea', 'Tarea'), ('practica', 'Práctica')], max_length=50),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='actividad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Actividad'),
        ),
        migrations.AddField(
            model_name='calificacion',
            name='seccionesalumno',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.SeccionesAlumno'),
        ),
    ]
