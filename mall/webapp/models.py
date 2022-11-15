from django.db import models

CHOICES = [('other', 'разное'), ('electronics', 'электроника'), ('clothes', 'одежда'), ('for_home', 'Для дома'),
           ('sports', 'спорт')]

class Stufs(models.Model):
    stuf = models.CharField(max_length=100, null=False, blank=True, verbose_name='stuf')
    description = models.TextField(max_length=2000, null=False, blank=False, verbose_name="description")
    categories = models.TextField(null=False, blank=True, choices=CHOICES,
                                  default=CHOICES[0][0],
                                  verbose_name="categories")
    remainder = models.PositiveIntegerField(null=False, blank=True, verbose_name="remainder")
    price = models.DecimalField(null=False, blank=True, max_digits=7, decimal_places=2, verbose_name="price")

    def __str__(self):
        return f'| {self.stuf} | {self.description} | {self.categories} | {self.remainder} | {self.price} |'
