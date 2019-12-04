from django.db import models as m
from django.shortcuts import reverse


class Order(m.Model):
    STATUS = (
        ('DONE', 'Выполнен'),
        ('UNDONE', 'Не выполнен'),
        ('CANCELED', 'Отменён')
    )
    name = m.CharField(max_length=100)
    amount = m.PositiveIntegerField()   # Кол-во изделий
    material = m.PositiveIntegerField()  # Кол-во материала на изделие
    status = m.CharField(choices=STATUS, max_length=8, default='UNDONE')
    client = m.ForeignKey('users.CustomUser', on_delete=m.CASCADE)

    def get_absolute_url(self):
        return reverse('core:order-detail', kwargs={'pk': self.pk})


class Base(m.Model):
    orders = m.ForeignKey(Order, on_delete=m.CASCADE)
    budget = m.IntegerField()
