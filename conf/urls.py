from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('core/', include('apps.core.urls'), name='core'),
    path('customers/', include('apps.customers.urls'), name='customers'),
    path('', include('apps.login.urls'), name='login'),
    path('todo/', include('apps.todo.urls'), name='todo'),
]
