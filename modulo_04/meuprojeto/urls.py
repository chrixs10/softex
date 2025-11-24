from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rota de login
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Rota de logout (A QUE FALTAVA!)
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),

    # Rotas do app core
    path('', include('core.urls')),
]
