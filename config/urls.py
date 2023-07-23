"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, include
# from pybo import views
from pybo.views import base_views


# pybo 에 views 에서 가져다 쓸때, -> django.urls 모듈로 include 를 가져와 사용하면 경로로 접근 가능
# from pybo import views

urlpatterns = [
    path('admin/', admin.site.urls),

    # pybo 에 views 에서 가져다 쓸때,
    # path('pybo/', views.index),

    # djanog.urls 에서 inlcude 를 사용하여 경로로 접근
    path('pybo/', include('pybo.urls')),
    path('common/', include('common.urls')),
    path('', base_views.index, name='index'),
]
