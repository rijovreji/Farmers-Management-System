"""
URL configuration for Farmer_Management_System project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib.staticfiles.urls import staticfiles_urlpatterns, static
from Farmer_Management_System import settings
from . import settings

from django.contrib import admin
from django.urls import path, include
import AdminApp.urls
import Farmer_Web.urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('AdminApp/', include(AdminApp.urls)),
    path('Farmer_Web/', include(Farmer_Web.urls))
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
