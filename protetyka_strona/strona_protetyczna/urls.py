from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='strona_glowna'),
    path('o-nas/', views.o_nas, name='o_nas'),
    path('cennik/', views.cennik, name='cennik'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('kontakt/', views.kontakt, name='kontakt'),
    path('oferty-pracy/', views.oferty_pracy, name='oferty_pracy'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('register/', views.register_view, name='register'),
    path('cennik/dodaj/', views.dodaj_cennik, name='dodaj_cennik'),
    path('cennik/edytuj/<int:pozycja_id>/', views.edytuj_cennik, name='edytuj_cennik'),
    path('cennik/usun/<int:pozycja_id>/', views.usun_cennik, name='usun_cennik'),
]