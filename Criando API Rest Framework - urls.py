from django.contrib import admin
from django.urls import path, include

# Criando as rotas da API
urlpatterns = [
    path('', include('api.urls')),
    path('admin/', admin.site.urls),
]
