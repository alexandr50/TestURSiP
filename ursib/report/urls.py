from django.urls import path
from .apps import ReportConfig
from .views import create_report, get_all_reports

app_name = ReportConfig.name

urlpatterns = [
    path('', create_report, name='create'),
    path('list_reports', get_all_reports, name='list_reports'),
]
