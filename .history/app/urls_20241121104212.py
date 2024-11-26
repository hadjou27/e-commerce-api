from django.urls import path
from app.views.user_views import UserRegisterView,CurrentUserView




urlpatterns = [
    path('user-profile/', CurrentUserView.as_view(), name='user-profile'),
    path('register/', UserRegisterView.as_view(), name='register'),
   ]