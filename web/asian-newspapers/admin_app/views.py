from django.shortcuts import render, HttpResponseRedirect, get_object_or_404
from django.contrib.auth.models import User
from main_app.models import Category, Newspaper
from main_app.forms import CategoryForm
from user_management_app.forms import MyRegistrationForm, UserChangeForm
from django.http import Http404, JsonResponse
from django.template import loader
from django.template.context_processors import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib.auth.decorators import user_passes_test


@user_passes_test(lambda u: u.is_superuser, login_url='/')
def admin_page(request):
    users = User.objects.all()
    return render(request, 'admin/admin_page.html', {'users': users})


def update_user(request, user_id):
    if request.is_ajax():
        if request.method == 'POST':
            user = get_object_or_404(User, id=user_id)
            form = UserChangeForm(request.POST or None, instance=user)
            if form.is_valid():
                form.save()
                print(user.username)
                return JsonResponse({
                    'errors': False,
                    'html': loader.render_to_string('inc-users_list.html', {'users': User.objects.all()})
                })
            else:
                print(user.first_name)
                errors = form.errors.as_json()
                return JsonResponse({'errors': errors})
    raise Http404


def get_user(request, user_id):
    if request.is_ajax():
        user = get_object_or_404(User, pk=user_id)
        form = UserChangeForm(instance=user)
        context = {'form': form,
                   'id': user_id}
        context.update(csrf(request))
        data = {'html': loader.render_to_string('inc-registration_form.html', context),
                'errors': False}
        return JsonResponse(data)
    raise Http404


def delete_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    user.delete()
    return HttpResponseRedirect('/admin')


def admin_categories(request):
    categories = Category.objects.all()
    paginator = Paginator(categories, 3)
    page = request.GET.get('page')
    try:
        categories = paginator.page(page)
    except PageNotAnInteger:
        categories = paginator.page(1)
    except EmptyPage:
        categories = paginator.page(paginator.num_pages)
    context = {'categories': categories}
    return render(request, 'admin/admin_categories.html', context)


def admin_categories_delete(request, id):
    category = get_object_or_404(Category, pk=id)
    category.delete()
    return HttpResponseRedirect('/admin/categories/')


def admin_categories_create(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/categories/')
        context = {'form': form}
        return render(request, 'admin/admin_category_create.html', context)
    context = {'form': CategoryForm()}
    return render(request, 'admin/admin_category_create.html', context)


def admin_categories_update(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    if request.method == 'POST':
        form = CategoryForm(request.POST, request.FILES, instance=category)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/admin/categories/')
        context = {'form': form}
        return render(request, 'admin/admin_category_update.html', context)
    context = {'form': CategoryForm(instance=category)}
    return render(request, 'admin/admin_category_update.html', context)


def admin_categories_detail(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    return render(request, 'admin/admin_category_detail.html', context={'category': category})
