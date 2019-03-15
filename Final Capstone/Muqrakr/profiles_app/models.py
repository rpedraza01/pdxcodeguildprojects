from django.db import models
from django.urls import reverse
from users_app.models import CustomUser

# create a user profile that is tied to the custom user class
class YourProfile(models.Model):
    user_name = models.ForeignKey('users_app.CustomUser', on_delete=models.CASCADE)
    user_title = models.CharField(max_length=50)
    about_user = models.CharField(max_length=512)
    user_pic = models.ImageField(upload_to='profile_pics')

# another would be saved candidate searches
class CandidateSearch(models.Model):
    candidate_name = models.CharField(max_length=100)
    user = models.ForeignKey('users_app.CustomUser', on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)

#another model would be saved committee searches
class CommitteeSearch(models.Model):
    committee_name = models.CharField(max_length=150)
    user = models.ForeignKey('users_app.CustomUser', on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)