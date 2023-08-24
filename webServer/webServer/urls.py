"""webServer URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from core import views
from django.conf import settings
from criticas.views import (OpinionListView , OpinionCreate, OpinionUpdate, OpinionDelete, OpinionDetailView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('contacto/',views.contacto,name='contacto'),
    path('contactar/',views.contactar),
    path('acercade/',views.acercade,name='acercade'),
    path('reviews/',OpinionListView.as_view(),name='reviews'),
    path('create/',OpinionCreate.as_view(),name='create'),
    path('update/<int:pk>/', OpinionUpdate.as_view(), name='update'),
    path('delete/<int:pk>/', OpinionDelete.as_view(), name='delete'),
    path('detail/<int:pk>', OpinionDetailView.as_view(), name='detail'),
]


#Configuración extendida para mostrar las imágenes
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
