from django.urls import path
from .views import SignupView
from django.contrib.auth.views import LoginView, LogoutView 


urlpatterns = [
    path('signup/', SignupView.as_view(), name='signup'),# постійно писати ас вю
    path('login/', LoginView.as_view(), name='login'),# тут свьо робить за нас джанго
    path('logout/', LogoutView.as_view(), name='logout'), # тут тоже
]
