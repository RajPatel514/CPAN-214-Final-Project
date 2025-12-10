from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('add/', views.add_book, name='add_book'),
    path('edit/<int:id>/', views.edit_book, name='edit_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('register/', views.register, name='register'),               
    path('login/', auth_views.LoginView.as_view(template_name='books/login.html'), name='login'),  
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'), 
    path('api/books/', views.api_get_books, name='api_books'),
    path('api/books/<int:id>/', views.api_get_book, name='api_book_detail'),
]
