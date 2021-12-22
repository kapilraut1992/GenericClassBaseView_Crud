from django.urls import path
from .views import Laptop_add,Laptop_show,Laptop_update,Laptop_delete


urlpatterns=[
    path('add/',Laptop_add.as_view(),name='add_laptop'),
    path('show/',Laptop_show.as_view(),name='show_laptop'),
    path('update/<int:pk>/',Laptop_update.as_view(),name='update_laptop'),
    path('delete/<int:pk>/',Laptop_delete.as_view(),name='delete_laptop'),
]