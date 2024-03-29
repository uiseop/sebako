"""sebako URL Configuration

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
    2. Add a URL to urlpatterns:  path('accounts/', include('accounts.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

import accounts.views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', accounts.views.home, name='home'),
    path('accounts/<int:pk>/',accounts.views.detail, name='detail'),
    # path('accounts/new/', accounts.views.new, name='new'),
    # path('accounts/create/', accounts.views.create, name='create'),
    # path('index/', accounts.views.index, name='index'),
    path('singlepage/',include('singlepage.urls')),
    path('resume/', include('resumes.urls')),
    path('managepage/',include('managepage.urls')),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)