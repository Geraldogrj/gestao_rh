# Generated by Django 4.0.2 on 2022-02-20 01:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('empregados', '0002_empregado_departamentos_empregado_empresa_and_more'),
        ('documentos', '0003_documento_detentor'),
    ]

    operations = [
        migrations.AlterField(
            model_name='documento',
            name='detentor',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='empregados.empregado'),
            preserve_default=False,
        ),
    ]