from django.urls import path
from . import views

urlpatterns = [ 
    path('', views.home),
    path('home', views.home),
    path('whatsapp_automation', views.whatsapp_automation),
    path('add_contact', views.add_contact),
    path('add_user_files', views.add_user_files),
    path('view_contacts', views.view_contacts),
    path('delete_images', views.delete_images),
]