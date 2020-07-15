from django.urls import path
from .views import register, PasswordChangeView, ProfilePageView, edit_settings

urlpatterns = [
    path('register/', register, name='register'),
    path('edit_settings/', edit_settings, name='edit_settings'),
    path('password/', PasswordChangeView.as_view(template_name='registration/password.html')),
    path('profile/<int:pk>', ProfilePageView.as_view(), name='profile'),
]
