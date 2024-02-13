from django.urls import path
from .views import *

urlpatterns = [
    path('', HomeNews.as_view(), name='home'),
    path('register', Register.as_view(), name='register'),
    path('login', Login_site.as_view(), name='login'),
    path('logout', Logout_site.as_view(), name='logout'),
    path('category/<int:category_id>', HomeCategory.as_view(), name='category'),
    path('news/<int:pk>', DetailNews.as_view(), name='news_view'),
    path('add_news', CreateNews.as_view(), name='add_news'),
]
