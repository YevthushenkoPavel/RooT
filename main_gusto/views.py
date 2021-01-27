from django.shortcuts import render
from .models import Category, Dish


# Create your views here.
def main(request):
    categories = Category.objects.filter(is_visible=True).order_by('category_order')
    for item in categories:
        item.dishes = Dish.objects.filter(category=item.pk)
    # categories = Category.objects.all()
    return render(request, 'index.html', context={'categories': categories})
