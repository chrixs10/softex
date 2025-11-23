from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    # Rota de login (ESSA É A QUE ESTÁ FALTANDO)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),

    # Inclui as rotas do app core
    path('', include('core.urls')),
]
