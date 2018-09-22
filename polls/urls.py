from django.urls import path
from . import views


app_name = 'polls'

urlpatterns = [
    #polls 애플리케이션에 대한 url/뷰 매핑을 정의하고 있습니다.
    path('', views.indexView.as_view(), name='index'),								#/polls/
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),			#/polls/5/
    path('<int:pk>/results/',views.ResultsView.as_view(), name='results'),	#/polls/5/results/
    path('<int:question_id>/vote/',views.vote, name='vote'),			#/polls/5/vote/
    path('test',views.test, name='test'),								#/polls/test
]