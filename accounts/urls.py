from django.urls import path
from accounts import views


urlpatterns = [
    path('login/', views.UserLoginView.as_view(), name="login"),
    path('register/', views.RegistrationView.as_view(), name="register"),
    path('logout/', views.logout_user, name='logout')
]
