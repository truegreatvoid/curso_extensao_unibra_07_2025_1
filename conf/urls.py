from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/core/', include('apps.core.urls'), name='core'),
    path('api/customers/', include('apps.customers.urls'), name='customers'),
    path('api/todo/', include('apps.todo.urls'), name='todo'),
]
