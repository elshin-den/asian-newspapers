from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Category, Newspaper, Banner
from django.shortcuts import get_object_or_404


def main(request):
    return render(request, 'index.html')


def newspapers(request):
    context = {'newspapers': Newspaper.objects.filter(is_website=False)}
    return render(request, 'newspapers.html', context)


def websites(request):
    context = {'newspapers': Newspaper.objects.filter(is_website=True)}
    return render(request, 'newspapers.html', context)


def category_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    newspapers = Newspaper.objects.filter(category__pk=category_id)
    context = {'category': category, 'newspapers': newspapers}
    return render(request, 'category_detail.html', context)


def newspaper_detail(request, newspaper_id):
    newspaper = get_object_or_404(Newspaper, pk=newspaper_id)
    banners = Banner.objects.filter(newspaper__pk=newspaper_id)
    context = {'newspaper': newspaper, 'banners': banners}
    return render(request, 'newspaper_detail.html', context)


def banner_detail(request, banner_id):
    banner = get_object_or_404(Banner, pk=banner_id)
    context = {'banner': banner}
    return render(request, 'banner_detail.html', context)


def contacts(request):
    return render(request, 'contacts.html')
