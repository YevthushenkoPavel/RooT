from django.shortcuts import render, redirect
from main_gusto.models import Dish, Category
from main_gusto.forms import CreateDish
from django.http import HttpResponse, HttpResponseNotFound
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.
def category(request, category):
    try:
        dishes = Dish.objects.filter(category=category)
        return render(request, 'dish.html', context={'category': dishes})
    except Dish.DoesNotExist:
        return HttpResponseNotFound("Page not found")


def dish(request, category, dish):
    dish = Dish.objects.get(pk=dish)
    return render(request, "dish_info.html", context={'dish': dish, 'category_id': category})


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
# Вывести все категории на страничку show-all-categories.html
def show_dishes(request):
    dishes = Dish.objects.all()
    context = {
        'dishes': dishes
    }
    return render(request, 'show-all-dishes.html', context)


class DishDetailView(DetailView):
    model = Dish
    template_name = 'dish-info.html'
    context_object_name = 'dish'


# Вывести форму для редактирования элемента
class DishUpdateView(UpdateView):
    model = Dish
    template_name = 'create-new-dish.html'
    form_class = CreateDish


# Вывести страничку для удаления категории
class DishDeleteView(DeleteView):
    model = Dish
    success_url = '/menu/dishes/'
    template_name = 'dish-delete.html'


@login_required(login_url='/login/')
@user_passes_test(lambda u: u.is_staff, login_url='/error/')
def create_new_dish(response):
    error = ''
    if response.method == 'POST':
        form = CreateDish(response.POST, response.FILES)
        if form.is_valid():
            form.save()
            return redirect("/menu/dishes/")
        else:
            error = 'Форма была не верной!'

    form = CreateDish()
    context = {
        'form': form,
        'error': error,
    }
    return render(response, 'create-new-dish.html', context)
