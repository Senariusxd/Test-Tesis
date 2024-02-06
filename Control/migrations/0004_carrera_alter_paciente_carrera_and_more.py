# Generated by Django 5.0.1 on 2024-02-06 03:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Control', '0003_paciente_carrera_alter_paciente_ocupacion'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='paciente',
            name='CARRERA',
            field=models.CharField(blank=True, default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='paciente',
            name='OCUPACION',
            field=models.CharField(choices=[('EST', 'Estudiante'), ('TRA', 'Trabajador')], max_length=255),
        ),
    ]