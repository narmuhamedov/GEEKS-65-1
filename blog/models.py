from django.db import models


class Fighter(models.Model):
    title = models.CharField(max_length=100, verbose_name='укажите имя бойца')
    photo = models.ImageField(upload_to='fighters/', verbose_name='загрузите фото бойца')
    KINDOM = (
        ('Земное царство', 'Земное царство'),
        ('Внешний мир', 'Внешний мир'),
        ('Преисподняя', 'Преисподняя'),
        ('Эдения', 'Эдения')
    )
    kindom = models.CharField(max_length=100, choices=KINDOM, verbose_name='укажите царство')
    description = models.TextField(verbose_name='укажите описание бойца')
    weapon = models.CharField(max_length=100, verbose_name="укажите оружие бойца", default='кунай')
    fatality = models.URLField(verbose_name='укажите ссылку на фаталити',null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        verbose_name = 'бойца'
        verbose_name_plural = 'бойцы МК'

    def __str__(self):
        return self.title



class FactsMk(models.Model):
    facts = models.CharField(max_length=100, verbose_name='укажите факт')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.facts} - {self.created_at}'