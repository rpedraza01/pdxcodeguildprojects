from django.urls import path

from . import views

app_name = 'profiles'
urlpatterns = [
	path('signup/', views.SignUpView.as_view(), name='signup'),
	path('user_homepage/', views.UserChirpListView.as_view(), name='user_homepage'),
]