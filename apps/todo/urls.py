from django.urls import path

from .views import CreateTaskView, DashboardView, UpdateStatusView

app_name = 'todo'

urlpatterns = [
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    path('create/', CreateTaskView.as_view(), name='create_task'),
    path('update-status/', UpdateStatusView.as_view(), name='update_status'),
]
