from django.urls import path, include
from . import views

urlpatterns = [
    path('register/', views.register),  # 레지스터 경로사용 + 함수
    path('login/', views.login),
    path('logout/', views.logout),
]
