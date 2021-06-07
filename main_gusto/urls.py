from django.urls import path
from main_gusto.views import main, show_category, create_new_category, \
    CategoryDeleteView, CategoryUpdateView, CategoryDetailView, \
    EventDeleteView, EventDetailView, EventUpdateView, create_new_event, show_events


urlpatterns = [
    path('', main, name='main'),
    path('categories/', show_category),
    path('categories/<int:pk>', CategoryDetailView.as_view(),
         name='category-details'),
    path('categories/<int:pk>/update',
         CategoryUpdateView.as_view(), name='category-update'),
    path('categories/<int:pk>/delete',
         CategoryDeleteView.as_view(), name='category-delete'),
    path('categories/create-new-category/', create_new_category),
    path('events/', show_events),
    path('events/<int:pk>', EventDetailView.as_view(), name='event-details'),
    path('events/<int:pk>/update', EventUpdateView.as_view(), name='event-update'),
    path('events/<int:pk>/delete', EventDeleteView.as_view(), name='event-delete'),
    path('events/create-new-event/', create_new_event),
]
