from django.urls import path,include
from . import views
app_name='obras'
urlpatterns = [
    path('',views.index,name='index'),
]
