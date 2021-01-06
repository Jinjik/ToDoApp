from django.db import models
from django.contrib.auth.models import User


class Organization(models.Model):
    name = models.CharField(max_length=100, verbose_name='Название организации')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Организация'
        verbose_name_plural = 'Организации'


class Employee(models.Model):
    user = models.OneToOneField(User, related_name='user', verbose_name='Сотрудник', on_delete=models.CASCADE)
    organization = models.ManyToManyField(Organization, related_name='employees', blank=True)
    login = models.ForeignKey(Organization, related_name='login', null=True, blank=True,
                              verbose_name='Авторизация в компании', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return self.user.email


class Task(models.Model):
    title = models.CharField(max_length=160, verbose_name='Название задачи')
    description = models.TextField(blank='True', null=True, verbose_name='Описание задачи')
    completed = models.BooleanField(default=False, blank=True, null=True, verbose_name='Статус')
    organization = models.ForeignKey(Organization, verbose_name="Организация", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Задача'
        verbose_name_plural = 'Задачи'


