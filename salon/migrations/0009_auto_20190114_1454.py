# Generated by Django 2.0.8 on 2019-01-14 20:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0008_auto_20190114_1443'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='escuela',
        ),
        migrations.AddField(
            model_name='user',
            name='escuela',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='salon.Escuela'),
        ),
    ]