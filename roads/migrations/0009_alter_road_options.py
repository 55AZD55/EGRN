# Generated by Django 5.2 on 2025-04-09 09:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0008_alter_road_property_law'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='road',
            options={'ordering': ['-ident_number']},
        ),
    ]
