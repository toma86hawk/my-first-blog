from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),   #post_listという名前にしたビューをルートURLに設定 ' 'はhttp..8000/ドメインを無視する
    path('post/<int:pk>/', views.post_detail, name='post_detail'),   #投稿の詳細ページのurlを設定
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]