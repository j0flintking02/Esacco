from django.urls import path

from . import views

urlpatterns = [
    path('', views.landingpage_view, name='landingpage'),
    path('esacco/dashboard/', views.dashboard_view, name='user_dashboard'),
    path('esacco/request/', views.request_view, name='request'),
    path('esacco/admin/dashboard', views.admin_dashboard_view, name='admin_dashboard'),
    path('esacco/admin/reports', views.admin_reports_view, name='admin_reports'),
]
