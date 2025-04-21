from django.db import models


class Road(models.Model):
    ident_number = models.CharField(max_length=20, default=52)
    name = models.CharField(max_length=200)
    kad_number = models.CharField(max_length=20)
    length = models.IntegerField()
    location = models.TextField()
    property_law = models.CharField(default='Оперативное управление', blank=True)
    document_foundation = models.TextField(default='')
    
    class Meta:
        ordering = ['ident_number']
    
    def __str__(self):
        return self.ident_number
    

class LandPlot(models.Model):
    kad_number = models.CharField(blank=True)
    
    CATEGORYS = (
        ('n', 'Земли населенных пунктов'),
        ('p', 'Земли промышленности'),
        ('s', 'Земли с/х назначения'),
        ('o', 'Земли особо охраняемых территорий'),
        ('l', 'Земли лесного фонда'),
        ('v', 'Земли водного фонда'),
        ('z', 'Земли запаса')
    )
    
    category = models.CharField(max_length=1, choices=CATEGORYS, default='p')
    
    VRI = (
        ('1.0', 'Сельскохозяйственное использование'),
        ('2.0', 'Жилая застройка'),
        ('3.0', 'Общественное использование объектов капитального строительства'),
        ('4.0', 'Предпринимательство'),
        ('5.0', 'Отдых (рекреация)'),
        ('6.0', 'Производственная деятельность'),
        ('6.1', 'Недропользование'),
        ('7.0', 'Транспорт'),
        ('7.2', 'Автомобильный транспорт'),
        ('12.0', 'Земельные участки (территории) общего пользования'),
        ('13.0', 'Земельные участки общего назначения'),
        ('0.0', 'Иное'),
        
    )
    
    vri = models.CharField(max_length=5, choices=VRI, default='a')
    location = models.TextField()
    square = models.IntegerField(default=1)
    property_law = models.CharField(default='Постоянное (бессрочное) пользование')
    road = models.ForeignKey('Road', on_delete=models.SET_NULL, null=True)
    document_foundation = models.TextField(default='')
    
    STATUS = (('1', 'Учтенный'), ('0', 'Снят с ГКУ'))
    
    status = models.CharField(max_length=1, choices=STATUS, default='1')
    
    def __str__(self):
        return self.kad_number
