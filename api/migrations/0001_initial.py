# Generated by Django 4.2.16 on 2024-12-03 17:00

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=254)),
                ('telefono', models.CharField(max_length=20)),
                ('recibir_alertas', models.BooleanField(default=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Mantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_realizacion', models.DateTimeField()),
                ('fecha_siguiente', models.DateTimeField()),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('realizado_por', models.CharField(blank=True, max_length=255, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado')], default='Pendiente', max_length=20)),
                ('costo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Modelo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.marca')),
            ],
        ),
        migrations.CreateModel(
            name='Taller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(blank=True, max_length=255, null=True)),
                ('telefono', models.CharField(max_length=20)),
                ('email', models.EmailField(blank=True, max_length=254, null=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='TipoServicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('costo_base', models.DecimalField(decimal_places=2, default=0.0, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='TipoVehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100, unique=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('placa', models.CharField(max_length=10, unique=True)),
                ('color', models.CharField(max_length=30)),
                ('año', models.PositiveIntegerField()),
                ('tipo_combustible', models.CharField(choices=[('Gasolina', 'Gasolina'), ('Diesel', 'Diesel'), ('Electrico', 'Eléctrico')], max_length=20)),
                ('vin', models.CharField(blank=True, max_length=50, null=True, unique=True)),
                ('ficha_tecnica', models.TextField(blank=True, null=True)),
                ('revision_tecnica', models.DateTimeField(blank=True, null=True)),
                ('fecha_registro', models.DateTimeField(auto_now_add=True)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True)),
                ('cliente', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.cliente')),
                ('marca', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.marca')),
                ('modelo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.modelo')),
                ('tipo', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tipovehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='Servicio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_servicio', models.DateTimeField(auto_now_add=True)),
                ('descripcion', models.TextField(blank=True, null=True)),
                ('costo', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('estado', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Completado', 'Completado')], default='Pendiente', max_length=20)),
                ('tipo_servicio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.tiposervicio')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='RecordatorioMantenimiento',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_recordatorio', models.DateTimeField(default=django.utils.timezone.now)),
                ('enviado', models.BooleanField(default=False)),
                ('mantenimiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.mantenimiento')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='tipo_servicio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.tiposervicio'),
        ),
        migrations.AddField(
            model_name='mantenimiento',
            name='vehiculo',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.vehiculo'),
        ),
        migrations.CreateModel(
            name='HistorialMensaje',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('estado_envio', models.CharField(choices=[('Exitoso', 'Exitoso'), ('Fallido', 'Fallido')], max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
        migrations.CreateModel(
            name='Falla',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descripcion', models.TextField()),
                ('fecha_reporte', models.DateTimeField(auto_now_add=True)),
                ('estado_falla', models.CharField(choices=[('Pendiente', 'Pendiente'), ('Resuelto', 'Resuelto')], default='Pendiente', max_length=50)),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.vehiculo')),
            ],
        ),
        migrations.CreateModel(
            name='ConfiguracionSistema',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('configuracion_alertas', models.BooleanField(default=True)),
                ('mensaje_ofertas', models.TextField(blank=True, null=True)),
                ('mensaje_mantenimiento', models.TextField(blank=True, null=True)),
                ('intervalo_alertas', models.IntegerField(default=30)),
                ('taller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.taller')),
            ],
        ),
        migrations.CreateModel(
            name='Alerta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('mensaje', models.TextField()),
                ('tipo_alerta', models.IntegerField(choices=[(1, 'Mantenimiento'), (2, 'Oferta'), (3, 'Recordatorio')])),
                ('fecha_envio', models.DateTimeField(auto_now_add=True)),
                ('estado', models.CharField(choices=[('Enviado', 'Enviado'), ('Pendiente', 'Pendiente')], default='Pendiente', max_length=20)),
                ('cliente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.cliente')),
            ],
        ),
    ]
