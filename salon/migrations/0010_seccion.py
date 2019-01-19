# Generated by Django 2.0.8 on 2019-01-16 02:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('salon', '0009_auto_20190114_1454'),
    ]

    operations = [
        migrations.CreateModel(
            name='Seccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('curso', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='salon.Curso')),
            ],
        ),
    ]
