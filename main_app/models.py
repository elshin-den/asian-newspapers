# -*- coding: utf-8 -*-
from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='category')

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Newspaper(models.Model):
    name = models.CharField(verbose_name='название', max_length=64, unique=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='newspaper')
    prices = models.TextField(verbose_name='цены', blank=True)
    discounts = models.TextField(verbose_name='скидки', blank=True)
    is_website = models.BooleanField(verbose_name='сайт', default=False)
    price_list = models.ImageField(verbose_name='прайс-лист', upload_to='price_list', blank=True)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name


class Banner(models.Model):
    newspaper = models.ForeignKey('Newspaper')
    size = models.CharField(verbose_name='размер', max_length=64, blank=True)
    description = models.TextField(verbose_name='описание', blank=True)
    image = models.ImageField(upload_to='banner')

    def __unicode__(self):
        return self.newspaper.name + ' ' + self.size

    def __str__(self):
        return self.newspaper.name + ' ' + self.size
