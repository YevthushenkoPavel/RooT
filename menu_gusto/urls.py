from django.urls import path
from .views import *


urlpatterns = [
    path('dishes/', show_dishes, name='dishes'),
    path('dishes/<int:pk>', DishDetailView.as_view(), name='dish-details'),
    path('dishes/<int:pk>/update', DishUpdateView.as_view(), name='dish-update'),
    path('dishes/<int:pk>/delete', DishDeleteView.as_view(), name='dish-delete'),
    path('dishes/create-new-dish/', create_new_dish),
]
