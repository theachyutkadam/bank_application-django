from django.urls import path
from account_type import views

urlpatterns = [
    path('', views.index),
    path('create', views.create, name='create-page'),
    path('new', views.new, name='new-page'),
    path('show/<int:id>', views.show, name="show-page"),
    path('edit/<int:id>', views.edit, name='edit-page'),
    path('update/<int:id>', views.update, name='update-page'),
    path('delete/<int:id>', views.destroy),
]
