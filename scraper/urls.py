from django.urls import path
from . import views

urlpatterns = [
    path('',views.response,name='response')
    # path('request/',views,name='requests'),
    # path('response/',views,name='response'),
]
