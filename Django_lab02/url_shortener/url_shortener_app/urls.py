from django.urls import path

from . import views

app_name = 'url_shortener_app'
urlpatterns = [
	path('', views.get_short_url, name='get_short_url'),
	path('submit_url', views.submit_url, name='submit_url'),
	path('redirect_user/<short_code>', views.redirect_user, name='redirect_user'),
]