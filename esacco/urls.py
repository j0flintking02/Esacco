from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingpage_view, name='landingpage'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('reports/', views.reports_view, name='reports'),
    path('request/', views.request_view, name='request'),
]
