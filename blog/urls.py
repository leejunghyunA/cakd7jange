# from . import views => 현재 폴더에 있는 views.py를 가져옴
from django.urls import path, include
from . import views

urlpatterns = [
    # url 정의
    path('create_post/', views.PostCreate.as_view()),
    path('category/<str:slug>/', views.category_page),
    path('tag/<str:slug>/', views.tag_page),
    path('<int:pk>/', views.PostDetail.as_view()),
    path('', views.PostList.as_view()), 
    # path('<int:pk>/', views.single_post_page),
    
# FBV방법(함수 기반)
    # path('', views.index), 
    ## =>views.py에 index() 함수를 실행
    # path('<int:pk>/', views.single_post_page),

]