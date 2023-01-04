from django.urls import path

from .views import RegisterCreateView, SignInView, LogoutView, ProfileView

urlpatterns = [
    path('signup/', RegisterCreateView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
    path('logaut/', LogoutView.as_view(), name='logaut'),
    path('accounts/profile/', ProfileView.as_view(), name='profile' )
]
