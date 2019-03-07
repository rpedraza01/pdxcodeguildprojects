from django.db import models
from django.urls import reverse

# Create your models here.
class Post(models.Model):
    author = models.CharField(null=True, blank=True, max_length=50)
    chirp_author = models.ForeignKey('auth.user', on_delete=models.CASCADE)
    chirp_title = models.CharField(null=True, blank=True, max_length=50)
    chirp_text = models.CharField(max_length=256)
    date_posted = models.DateTimeField(auto_now_add=True)
    date_edited = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.chirp_title

    def get_absolute_url(self):
        return reverse('chirp_posts_app:chirp_detail', args=[str(self.id)])