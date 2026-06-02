from django.db import models

class Games(models.Model):
    title = models.CharField(max_length=100, verbose_name='введите название игры')
    photo = models.ImageField(upload_to='games/', verbose_name='загрузите фото')
    description = models.TextField(verbose_name='укажите описание игры', blank=True)
    url = models.URLField(verbose_name='укажите ссылку для скачивания игры')