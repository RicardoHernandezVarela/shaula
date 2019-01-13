# Generated by Django 2.0.8 on 2019-01-11 08:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0005_auto_20190111_0215'),
    ]

    operations = [
        migrations.AddField(
            model_name='grupo',
            name='id',
            field=models.AutoField(auto_created=True, default=1, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='grupo',
            name='escuela',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Escuela'),
        ),
    ]
