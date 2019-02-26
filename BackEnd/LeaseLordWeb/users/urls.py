from django.urls import path
from users import views
from django.contrib.auth import views as auth_views

urlpatterns = [
   path('register/', views.registercheck),
   path('login/', auth_views.LoginView.as_view()),
   path('registerten/',views.registerten),
]
