from django.db import models
from django.core.exceptions import ValidationError

def validate_positive(value):
    if value < 0:
        raise ValidationError('Значение должно быть положительным')

class Product(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    description = models.TextField(verbose_name='Описание')
    price = models.IntegerField(verbose_name='Цена', validators=[validate_positive])
    quantity = models.IntegerField(verbose_name='Количество' ,validators=[validate_positive])
    
    def __str__(self):
        return f'{self.title}'
    
    class Meta:
        verbose_name = 'Товар'
        verbose_name_plural = 'Товары'