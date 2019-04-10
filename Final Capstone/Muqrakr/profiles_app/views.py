from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy, reverse
from django.views.generic import TemplateView, ListView
from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .forms import ProfileForm
import json, csv

from .models import YourProfile, CandidateSearch, CommitteeSearch


class HomePageView(TemplateView):
    success_url = reverse_lazy('homepage')
    template_name = 'homepage.html'


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
    # template_name = 'search.html'
    query = json.loads(request.body)
    print(query)
    CandidateSearch.objects.create(
        name=query['name'],
        user=request.user,
        party=query['party'],
        office_address=f"{query['mailing_address']}, {query['mailing_city']}, {query['mailing_state']}, {query['mailing_zip']}",
        total_receipts=query['total_receipts'],
        total_cont_ind=query['total_from_individuals'],
        total_cont_pacs=query['total_from_pacs'],
        total_cont=query['total_contributions'],
        total_loans=query['candidate_loans'],
        total_disbursements=query['total_disbursements'],
        begin_cash=query['begin_cash'],
        end_cash=query['end_cash'],
        total_refunds=query['total_refunds'],
        debts_owed=query['debts_owed'],
        ind_expend=query['independent_expenditures'],
        coord_expend=query['coordinated_expenditures'],
        begin_info_date=query['date_coverage_from'],
        final_info_date=query['date_coverage_to'],
        )
    return HttpResponse(request.body)


@csrf_exempt
def ajax_save_search_committee(request):
    # template_name = 'search.html'
    query = json.loads(request.body)
    print(query)
    CommitteeSearch.objects.create(
        committee_name=query['name'],
        user=request.user,
        party=query['party'],
        comm_treasurer=query['treasurer'],
        comm_address=f"{query['address']}, {query['city']}, {query['state']}, {query['zip']}",
        total_receipts=query['total_receipts'],
        total_cont_ind=query['total_from_individuals'],
        total_cont_pacs=query['total_from_pacs'],
        total_cont=query['total_contributions'],
        # total_loans = query[''],
        total_disbursements=query['total_disbursements'],
        begin_cash=query['begin_cash'],
        end_cash=query['end_cash'],
        total_refunds=query['total_refunds'],
        debts_owed=query['debts_owed'],
        ind_expend=query['total_independent_expenditures'],
        coord_expend=query['total_candidate_contributions'],
        begin_info_date=query['date_coverage_from'],
        final_info_date=query['date_coverage_to'],
        )
    return HttpResponse(request.body)


class YourProfileView(LoginRequiredMixin, ListView):
    # success_url = reverse_lazy('your_profile')
    context_object_name = 'candidatesearch'
    template_name = 'your_profile.html'

    def get_queryset(self):
        return CandidateSearch.objects.filter(user=self.request.user)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['committeesearch_list'] = CommitteeSearch.objects.filter(user=self.request.user)
        return context


def delete_candidate(request):
    for id in request.POST.getlist('checkbox'):
        get_object_or_404(CandidateSearch, pk=id).delete()
    return HttpResponseRedirect(reverse('profiles_app:your_profile'))

def delete_committee(request):
    for id in request.POST.getlist('checkbox'):
        get_object_or_404(CommitteeSearch, pk=id).delete()
    return HttpResponseRedirect(reverse('profiles_app:your_profile'))

def save_search_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="candidatesearch.csv"'
    candidates = CandidateSearch.objects.filter(user=request.user)
    writer = csv.writer(response)
    writer.writerow([
        'Name',
        'Party',
        'Office Address',
        'Total Receipts',
        'Total Individual Contributions',
        'Total PAC Contributions',
        'Total Contributions',
        'Total Loans',
        'Total Disbursements',
        'Beginning Cash',
        'Ending Cash',
        'Total Refunds',
        'Debts Owed',
        'Independent Expenditures',
        'Coordinated Expenditures',
        'Filing Date'
        ])
    for id in request.POST.getlist('checkbox'):
        candidate = get_object_or_404(CandidateSearch, pk=id)
        writer.writerow([
            candidate.name,
            candidate.party,
            candidate.office_address,
            candidate.total_receipts,
            candidate.total_cont_ind,
            candidate.total_cont_pacs,
            candidate.total_cont,
            candidate.total_loans,
            candidate.total_disbursements,
            candidate.begin_cash,
            candidate.end_cash,
            candidate.total_refunds,
            candidate.debts_owed,
            candidate.ind_expend,
            candidate.coord_expend,
            candidate.begin_info_date,
            ])
    return response

def save_search_committee_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="committeesearch.csv"'
    committees = CommitteeSearch.objects.filter(user=request.user)
    writer = csv.writer(response)
    writer.writerow([
        'Committee Name',
        'Party',
        'Treasurer',
        'Office Address',
        'Total Receipts',
        'Total Individual Contributions',
        'Total PAC Contributions',
        'Total Contributions',
        'Total Disbursements',
        'Beginning Cash',
        'Ending Cash',
        'Total Refunds',
        'Debts Owed',
        'Independent Expenditures',
        'Coordinated Expenditures',
        'Filing Date'
        ])
    for id in request.POST.getlist('checkbox'):
        committee = get_object_or_404(CommitteeSearch, pk=id)
        writer.writerow([
            committee.committee_name,
            committee.party,
            committee.comm_treasurer,
            committee.comm_address,
            committee.total_receipts,
            committee.total_cont_ind,
            committee.total_cont_pacs,
            committee.total_cont,
            committee.total_disbursements,
            committee.begin_cash,
            committee.end_cash,
            committee.total_refunds,
            committee.debts_owed,
            committee.ind_expend,
            committee.coord_expend,
            committee.begin_info_date,
            ])
    return response


class CreateYourProfile(LoginRequiredMixin, CreateView):
    model = YourProfile
    template_name = 'create_your_profile.html'
    form_class = ProfileForm
    # fields = ['user_title', 'about_user', 'user_pic']
    login_url = 'login'
    success_url = reverse_lazy('your_profile.html')

    def form_valid(self, form):
        form.instance.user_name = self.request.users_app.CustomUser
        return super().form_valid(form)


class UpdateYourProfile(LoginRequiredMixin, UpdateView):
    model = YourProfile
    template_name = 'update_your_profile.html'
    form_class = ProfileForm
    # fields = ['user_pic', 'user_title', 'about_user']
    success_url = reverse_lazy('profiles_app:your_profile')

    def form_valid(self, form):
        form.instance.user_name = self.request.user
        return super().form_valid(form)

    def get_object(self, queryset=None):
        return self.request.user