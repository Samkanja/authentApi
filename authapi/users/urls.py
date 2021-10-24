from django.contrib import admin
from django.urls import path
from .views import LoginView, RegistraionView, LoginView,UserView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register', RegistraionView.as_view()),
    path('login', LoginView.as_view()),
    path('user',UserView.as_view()),
    path('logout', LogoutView.as_view())
]

