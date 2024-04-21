from django.db import models

# Create your models here.

class PortfolioItem(models.Model):
    img = models.ImageField(verbose_name="Изображение")
    text = models.TextField(verbose_name="Текст")

    class Meta:
        verbose_name = 'Портфолио'
        verbose_name_plural = 'Портфолио'

    def __str__(self):
        return f'Портфолио № {self.id}'


class ServiceItem(models.Model):
    img = models.ImageField(verbose_name="Изображение")
    title = models.TextField(verbose_name="Наименование", max_length=255)

    
    class Meta:
        verbose_name = 'Услуга'
        verbose_name_plural = 'Услуг'
    
    def __str__(self):
        return f'Услуга № {self.id}'