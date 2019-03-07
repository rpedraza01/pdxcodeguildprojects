from django.urls import path

from . import views

app_name = 'chirp_posts_app'
urlpatterns = [
	path('', views.ChirpListView.as_view(), name='homepage'),
	path('chirp_detail/', views.ChirpDetailView.as_view(), name='chirp_detail'),
	path('chirp_new/', views.ChirpCreateView.as_view(), name='chirp_new'),
	path('chirp_update/<int:pk>', views.ChirpUpdateView.as_view(), name='chirp_update'),
	path('chirp_delete/<int:pk>', views.ChirpDeleteView.as_view(), name='chirp_delete'),
	# path('author/<author>', views.UserChirpListView.as_view(), name='author'),
]