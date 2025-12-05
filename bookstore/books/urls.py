from django.urls import path
from . import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:id>/', views.edit_book, name='edit_book'),

]
