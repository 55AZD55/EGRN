# Generated by Django 5.2 on 2025-04-09 09:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('roads', '0006_remove_landplot_road_landplot_road'),
    ]

    operations = [
        migrations.AlterField(
            model_name='landplot',
            name='category',
            field=models.CharField(choices=[('n', 'Земли населенных пунктов'), ('p', 'Земли промышленности'), ('s', 'Земли с/х назначения'), ('o', 'Земли особо охраняемых территорий'), ('l', 'Земли лесного фонда'), ('v', 'Земли водного фонда'), ('z', 'Земли запаса')], default='p', max_length=1),
        ),
        migrations.AlterField(
            model_name='landplot',
            name='vri',
            field=models.CharField(choices=[('1.0', 'Сельскохозяйственное использование'), ('2.0', 'Жилая застройка'), ('3.0', 'Общественное использование объектов капитального строительства'), ('4.0', 'Предпринимательство'), ('5.0', 'Отдых (рекреация)'), ('6.0', 'Производственная деятельность'), ('6.1', 'Недропользование'), ('7.0', 'Транспорт'), ('7.2', 'Автомобильный транспорт'), ('12.0', 'Земельные участки (территории) общего пользования'), ('13.0', 'Земельные участки общего назначения'), ('0.0', 'Иное')], default='a', max_length=5),
        ),
    ]
