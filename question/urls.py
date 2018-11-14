from django.urls import path
from . import views

app_name = 'question'

urlpatterns = [
    path('', views.list, name='list'),
    path('create/', views.create, name='create'),   # 앞에는 모두 questions가 생략되어 있음
    path('<int:id>/detail/', views.detail, name='detail'),
    path('<int:id>/comment/create', views.comment_create, name='comment_create'),
    path('<int:id>/update/', views.update, name='update'),
    path('<int:id>/delete/', views.delete, name='delete'),
    # path('<int:id>/comment/update', views.comment_update, name='comment_update'),
    # path('<int:id>/comment/delete', views.comment_delete, name='comment_delete'),
]




