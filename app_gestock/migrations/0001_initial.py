# Generated by Django 4.2 on 2023-05-24 09:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='t_article',
            fields=[
                ('idArticle', models.AutoField(primary_key=True, serialize=False)),
                ('artName', models.CharField(max_length=50)),
                ('artNote', models.CharField(max_length=250)),
            ],
        ),
        migrations.CreateModel(
            name='t_categories',
            fields=[
                ('idCategories', models.AutoField(primary_key=True, serialize=False)),
                ('catName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_cupboard',
            fields=[
                ('idCupboard', models.AutoField(primary_key=True, serialize=False)),
                ('cupName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_room',
            fields=[
                ('idRoom', models.AutoField(primary_key=True, serialize=False)),
                ('rooName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_types',
            fields=[
                ('idType', models.AutoField(primary_key=True, serialize=False)),
                ('typName', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='t_products',
            fields=[
                ('idProduct', models.AutoField(primary_key=True, serialize=False)),
                ('proName', models.CharField(max_length=75)),
                ('proNote', models.CharField(max_length=250)),
                ('proImage', models.CharField(max_length=500)),
                ('proBoughtPrice', models.FloatField()),
                ('proBoughtDate', models.DateField()),
                ('fkArticle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestock.t_article')),
                ('fkCategory', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestock.t_categories')),
                ('fkCupboard', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestock.t_cupboard')),
                ('fkType', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_gestock.t_types')),
            ],
        ),
        migrations.CreateModel(
            name='t_borrow',
            fields=[
                ('idBorrow', models.AutoField(primary_key=True, serialize=False)),
                ('borLocation', models.CharField(max_length=50)),
                ('borDate', models.DateField()),
                ('borReturnDate', models.DateField()),
                ('borNote', models.CharField(max_length=250)),
                ('borUser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
