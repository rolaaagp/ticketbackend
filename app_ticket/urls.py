from django.urls import path

from .views import views_status, views_ticket

urlpatterns = [
    path('status/', views_status.StatusAPIView.as_view()),
    path('', views_ticket.TicketAPIView.as_view()),

]
