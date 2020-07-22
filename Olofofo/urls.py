from django.urls import path
from . import views


urlpatterns = [
    path('news', views.news_list, name='news'),
    path('', views.index_list, name='index'),
    path('entertainment', views.entertainment_list, name='entertainment'),
    path('sports', views.sports_list, name='sports'),
    path('world_news', views.world_news_list, name='world_news'),
    path('<str:slug>/', views.post_details_view, name='post_details'),
    ]
