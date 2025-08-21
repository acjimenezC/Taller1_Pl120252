from django.urls import path
from . import views

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('statistics/', views.statistics_genre_view, name='statistics'),
    path('statistics/genre/', views.statistics_genre_view, name='statistics_genre'),  # <-- agrega esta línea
]