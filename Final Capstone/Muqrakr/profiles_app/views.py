from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse#, JsonResponse
from django.template import Context, loader
from django.views.decorators.csrf import csrf_exempt
import json

from .models import YourProfile, CandidateSearch, CommitteeSearch

class HomePageView(TemplateView):
    success_url = reverse_lazy('home')
    template_name = 'home.html'

class AboutView(TemplateView):
    # success_url = reverse_lazy('about')
    template_name = 'about.html'

class IntroToCFView(TemplateView):
    # success_url = reverse_lazy('intro_to_cf')
    template_name = 'intro_to_cf.html'

class SearchView(TemplateView):
    # success_url = reverse_lazy('search')
    template_name = 'search.html'

@csrf_exempt
def ajax_save_search(request):
    query = json.loads(request.body)
    print(query)
    CandidateSearch.objects.create(
        name = query['name'],
        user = request.user,
        party = query['party'],
        office_address = f"{query['mailing_address']}, {query['mailing_city']}, {query['mailing_state']}, {query['mailing_zip']}",
        total_receipts = query['total_receipts'],
        total_cont_ind = query['total_from_individuals'],
        total_cont_pacs = query['total_from_pacs'],
        total_cont = query['total_contributions'],
        total_loans = query['candidate_loans'],
        total_disbursements = query['total_disbursements'],
        begin_cash = query['begin_cash'],
        end_cash = query['end_cash'],
        total_refunds = query['total_refunds'],
        debts_owed = query['debts_owed'],
        ind_expend = query['independent_expenditures'],
        coord_expend = query['coordinated_expenditures'],
        begin_info_date = query['date_coverage_from'],
        final_info_date = query['date_coverage_to'],
        )
    return HttpResponse(request.body)

class YourProfileView(LoginRequiredMixin, TemplateView):
    # success_url = reverse_lazy('your_profile')
    template_name = 'your_profile.html'

class CreateYourProfile(LoginRequiredMixin, CreateView):
    model = YourProfile
    template_name = 'create_your_profile.html'
    fields = ['user_title', 'about_user', 'user_pic']
    login_url = 'login'
    success_url = reverse_lazy('your_profile.html')

    def form_valid(self, form):
        form.instance.user_name = self.request.users_app.CustomUser
        return super().form_valid(form)

class UpdateYourProfile(LoginRequiredMixin, UpdateView):
    model = YourProfile
    template_name = 'update_your_profile.html'
    fields = ['user_title', 'about_user', 'user_pic']
    success_url = reverse_lazy('your_profile.html')