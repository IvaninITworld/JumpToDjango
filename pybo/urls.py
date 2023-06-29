from django.urls import path

from . import views

urlpatterns= [
    path('', views.index())
#config/urls.py 파일에서 이미 pybo/로 시작하는 URL이 pybo/urls.py 파일과 먼저 매핑 그래서 ''으로시작
]