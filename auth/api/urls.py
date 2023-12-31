from django.urls import path
from .views import *

urlpatterns = [
    path('user/', UserView.as_view()), 
    path('login/', LoginAPI.as_view()), 
    path('register/', RegisterAPI.as_view()), 
    path('logout/', LogoutAPI.as_view()), 
]