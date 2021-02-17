from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
    ('NEW', 'New Site'),
    ('EX', 'Existing Site'),
)

PRIORITY_CHOICES = (
    ('U', 'Urgent - 1 week or less'),
    ('N', 'Normal - 2 - 4 weeks'),
    ('L', 'Low - Still Researching'),
)


class Quote(models.Model):
    name = models.CharField(max_length=100, verbose_name='Имя')
    position = models.CharField(max_length=60, blank=True, verbose_name='Позиция')
    company = models.CharField(max_length=60, blank=True, verbose_name='Компания')
    address = models.CharField(max_length=200, blank=True, verbose_name='Адрес')
    phone = models.CharField(max_length=30, blank=True, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Е-Майл')
    web = models.URLField(blank=True, verbose_name='Сайт')
    description = models.TextField(verbose_name='Текст')
    sitestatus = models.CharField(max_length=20, choices=STATUS_CHOICES, verbose_name='Статус сайта')
    priority = models.CharField(max_length=40, choices=PRIORITY_CHOICES, verbose_name='Приоритет')
    jobfile = models.FileField(upload_to='uploads/', verbose_name='Файл')
    submitted = models.DateField(auto_now_add=True, verbose_name='Представление')
    quotedate = models.DateField(blank=True, null=True, verbose_name='Дата создания')
    quoteprice = models.DecimalField(decimal_places=2, max_digits=7, blank=True, default=0, verbose_name='Цена')
    username = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
# TODO: Нужно будет сделать перевод на Румынский
    def __str__(self):
        return str(self.id)
