# Generated by Django 4.0.6 on 2022-07-13 13:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('anamneses', '0005_alter_anamnese_criado_em'),
    ]

    operations = [
        migrations.AlterField(
            model_name='anamnese',
            name='criado_em',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
