from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('statistics/', views.statistics_view, name='statistics'),
]