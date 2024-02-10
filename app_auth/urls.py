from django.urls import path

from .views import LogoutAPIView, LoginAPIView

urlpatterns = [
    path('login/', LoginAPIView.as_view(), name='login'),
    path('logout/', LogoutAPIView.as_view(), name='logout'),

]
