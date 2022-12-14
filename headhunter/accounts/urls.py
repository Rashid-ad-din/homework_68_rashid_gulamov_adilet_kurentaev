from django.urls import path

from accounts.views import LoginView, LogoutView, RegisterView, ProfileView, UserChangeView, PasswordChangeView


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', RegisterView.as_view(), name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/change/', UserChangeView.as_view(), name='change'),
    path('profile/password-change/', PasswordChangeView.as_view(), name='password_change'),
]
