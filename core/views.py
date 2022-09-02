from django.shortcuts import render, HttpResponse
from .models import Bootle


def contacts(request):
    return render(request, 'core/contacts.html')

def about(request):
    return render(request, 'about.html')

def makers_list(request):
    context = {}
    bottles_list = Bootle.objects.all()
    context['bottles_list'] = bottles_list
    html_page = render(request, 'makers.html', context)
    return html_page


