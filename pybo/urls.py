from django.urls import path

from . import views

# namesapce 추가
app_name = 'pybo'

urlpatterns = [
    # # 다만 path('', views.index) 처럼 pybo/ 가 생략된 '' 이 사용되었다.
    # # 이렇게 되는 이유는 config/urls.py 파일에서 이미 pybo/로 시작하는
    # # URL이 pybo/urls.py 파일과 먼저 매핑되었기 때문이다.
    # path('', views.index),
    # path('<int:question_id>/', views.detail),

    # 위와 같이 사용할 수 도 있지만 별칭을 이용해서 url 사용이 가능하다.
    path('', views.index, name='index'),
    path('<int:question_id>/', views.detail, name='detail'),
    path('answer/create/<int:question_id>/', views.answer_create, name='answer_create'),

    path('question/create/', views.question_create, name='question_create'),
]
