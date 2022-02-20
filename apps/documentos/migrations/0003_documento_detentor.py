# Generated by Django 4.0.2 on 2022-02-20 01:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empregados', '0001_initial'),
        ('documentos', '0002_alter_documento_descricao'),
    ]

    operations = [
        migrations.AddField(
            model_name='documento',
            name='detentor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='empregados.empregado'),
        ),
    ]