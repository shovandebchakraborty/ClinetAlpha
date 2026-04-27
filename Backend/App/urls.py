"""
URL configuration for Backend project.

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
from django.urls import path,include
from .views import *
urlpatterns = [
    path('datauploadapi/',DataUploadAPI,name="data_upload_api"),
    path('dataviewapi/',DataViewAPI,name="data_view_api"),
    path('datadeleteapi/<int:id>/', DataDeleteAPI, name="data_delete_api")
]
