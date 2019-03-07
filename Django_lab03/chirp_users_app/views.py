from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from chirp_posts_app.models import Post
from django.contrib.auth.models import User

class SignUpView(generic.CreateView):
	form_class = UserCreationForm
	template_name = 'chirp_users_app/registration.html'
	success_url = reverse_lazy('chirp_posts_app:homepage')

class UserChirpListView(generic.ListView):
	model = Post
	template_name = 'chirp_posts_app/user_homepage.html'

	def get_queryset(self):
		# if self.chirp_author 
		if self.request.user.is_authenticated:
			return Post.objects.filter(chirp_author=self.request.user)
		return Post.objects.all()