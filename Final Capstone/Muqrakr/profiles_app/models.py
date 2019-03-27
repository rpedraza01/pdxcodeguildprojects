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
    name = models.CharField(null=True, blank=True, max_length=100, default='')
    user = models.ForeignKey('users_app.CustomUser', on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)
    party = models.CharField(null=True, blank=True, max_length=150, default='')
    office_address = models.CharField(null=True, blank=True, max_length=150, default='')
    total_receipts = models.IntegerField(null=True, blank=True, default=0)
    total_cont_ind = models.IntegerField(null=True, blank=True, default=0)
    total_cont_pacs = models.IntegerField(null=True, blank=True, default=0)
    total_cont = models.IntegerField(null=True, blank=True, default=0)
    total_loans = models.IntegerField(null=True, blank=True, default=0)
    total_disbursements = models.IntegerField(null=True, blank=True, default=0)
    begin_cash = models.IntegerField(null=True, blank=True, default=0)
    end_cash = models.IntegerField(null=True, blank=True, default=0)
    total_refunds = models.IntegerField(null=True, blank=True, default=0)
    debts_owed = models.IntegerField(null=True, blank=True, default=0)
    ind_expend = models.IntegerField(null=True, blank=True, default=0)
    coord_expend = models.IntegerField(null=True, blank=True, default=0)
    begin_info_date = models.CharField(null=True, blank=True, max_length=12, default='')
    final_info_date = models.CharField(null=True, blank=True, max_length=12, default='')

    class Meta:
        verbose_name_plural = "Candidate Searches"

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('Muqrakr:your_profile', args=[str(self.id)])

#another model would be saved committee searches
class CommitteeSearch(models.Model):
    committee_name = models.CharField(null=True, blank=True, max_length=150, default='')
    user = models.ForeignKey('users_app.CustomUser', on_delete=models.CASCADE)
    date_saved = models.DateTimeField(auto_now_add=True)
    party = models.CharField(null=True, blank=True, max_length=150, default='')
    comm_treasurer = models.CharField(null=True, blank=True, max_length=150, default='')
    comm_address = models.CharField(null=True, blank=True, max_length=150, default='')
    total_receipts = models.IntegerField(null=True, blank=True, default=0)
    total_cont_ind = models.IntegerField(null=True, blank=True, default=0)
    total_cont_pacs = models.IntegerField(null=True, blank=True, default=0)
    total_cont = models.IntegerField(null=True, blank=True, default=0)
    total_loans = models.IntegerField(null=True, blank=True, default=0)
    total_disbursements = models.IntegerField(null=True, blank=True, default=0)
    begin_cash = models.IntegerField(null=True, blank=True, default=0)
    end_cash = models.IntegerField(null=True, blank=True, default=0)
    total_refunds = models.IntegerField(null=True, blank=True, default=0)
    debts_owed = models.IntegerField(null=True, blank=True, default=0)
    ind_expend = models.IntegerField(null=True, blank=True, default=0)
    coord_expend = models.IntegerField(null=True, blank=True, default=0)
    begin_info_date = models.CharField(null=True, blank=True, max_length=12, default='')
    final_info_date = models.CharField(null=True, blank=True, max_length=12, default='')

    class Meta:
        verbose_name_plural = "Committee Searches"

    def __str__(self):
        return self.committee_name

    def get_absolute_url(self):
        return reverse('Muqrakr:your_profile', args=[str(self.id)])