from django.contrib.auth import views as auth_views
from django.contrib import admin
from django.urls import path, include
from django.shortcuts import render

urlpatterns = [
    path('admin/', admin.site.urls),
    path('cart/', include('cart.urls')),
    path('orders/', include('orders.urls')),
    path('payments/', include('payments.urls')),
    path('products/', include('products.urls')),
    path('reviews/', include('reviews.urls')),
    path('users/', include('users.urls')),

    path('homepage/', lambda request: render(request, 'homepage.html'), name='homepage'),
    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
]
