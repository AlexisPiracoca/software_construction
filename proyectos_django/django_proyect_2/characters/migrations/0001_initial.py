# Generated by Django 3.2.7 on 2021-11-01 01:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Character',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=500)),
                ('path', models.FileField(upload_to='')),
                ('date_of_birth', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'characters',
            },
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'db_table': 'city',
            },
        ),
        migrations.CreateModel(
            name='Power',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'powers',
            },
        ),
        migrations.CreateModel(
            name='Universe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=2000)),
                ('foundation', models.CharField(max_length=100)),
            ],
            options={
                'db_table': 'universes',
            },
        ),
        migrations.CreateModel(
            name='PowerCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('level', models.FloatField()),
                ('cha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.character')),
                ('pow', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.power')),
            ],
            options={
                'db_table': 'powers_character',
            },
        ),
        migrations.AddField(
            model_name='character',
            name='cit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.city'),
        ),
        migrations.AddField(
            model_name='character',
            name='uni',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='characters.universe'),
        ),
    ]
