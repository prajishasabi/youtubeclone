from django.urls import path
from . import views
app_name ='index'
urlpatterns=[
    path('',views.index_home,name='index_home'),
    path('trending',views.index_trend,name='trending'),
     path('subscription',views.index_sub,name='subscription')
]
