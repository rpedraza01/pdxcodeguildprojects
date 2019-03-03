from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.urls import reverse
import random
import string

from .models import ShortURLs
# Create your views here.

model = ShortURLs
template_name = "url_shortener_app/index.html"

def get_short_url(request):
    short_url_list = ShortURLs.objects.filter().order_by()
    context = {
        'short_url_list':short_url_list,
    }
    return render(request, 'url_shortener_app/index.html', context)

def submit_url(request):
    url_chars = string.ascii_lowercase + string.ascii_uppercase + string.digits
    short_code = "".join([random.choice(url_chars)for i in range(6)])
    long_url = request.POST["URL-text"]
    new_url = ShortURLs(short_code=short_code, long_url=long_url)
    new_url.save()
    return HttpResponseRedirect(reverse('url_shortener_app:get_short_url'))

def redirect_user(request, short_code):
    item = get_object_or_404(ShortURLs, short_code=short_code)
    if item.number_of_clicks == "null":
        item.number_of_clicks = 1
    else:
        item.number_of_clicks += 1
    item.save()
    return HttpResponseRedirect(item.long_url)