from django.contrib import admin
from django.urls import path
from account_type import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('index', views.index),
    path('create', views.create),
    path('show', views.show),
    path('edit/<int:id>', views.edit),
    path('update/<int:id>', views.update),
    path('delete/<int:id>', views.destroy),
]
