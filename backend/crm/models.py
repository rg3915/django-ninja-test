from django.db import models


class Customer(models.Model):
    name = models.CharField('nome', max_length=100)
    active = models.BooleanField('ativo',default=True)
    
    class Meta:
        ordering = ('name',)
        verbose_name = 'cliente'
        verbose_name_plural = 'clientes'
    
    def __str__(self):
        return f'{self.name}'
    