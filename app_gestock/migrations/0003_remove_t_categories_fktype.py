# Generated by Django 4.2 on 2023-05-24 13:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_gestock', '0002_remove_t_products_fkcupboard_t_article_fkcupboard_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='t_categories',
            name='fkType',
        ),
    ]