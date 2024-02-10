from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ticket/', include('app_ticket.urls')),
    path('auth/', include('app_auth.urls'))
]
