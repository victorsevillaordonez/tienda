# Generated by Django 2.1 on 2018-08-22 17:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Categoria',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Marca',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('precio', models.IntegerField()),
                ('stock', models.IntegerField()),
                ('status', models.BooleanField(default=True)),
                ('foto', models.ImageField(blank=True, null=True, upload_to='fotos')),
                ('categoria', models.ManyToManyField(blank=True, null=True, to='home.Categoria')),
                ('marca', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='home.Marca')),
            ],
        ),
    ]
