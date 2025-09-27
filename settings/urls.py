from django.contrib import admin
from django.urls import path
from apps.cards.views import index
from apps.cards.views import users_list,city_time,counter_view


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index,name = 'index'),
    path('users/', users_list,name = 'users_list'),
    path('city_time/', city_time,name = 'city_time'),
    path('cnt/', counter_view, name='counter'),
]