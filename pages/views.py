from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.mail import send_mail, get_connection

from .models import Page
from .forms import ContactForm


def index(request):
    return render(request, 'base.html')


def pageindex(request, pagename):
    pg = get_object_or_404(Page, permalink=pagename)
    # pg = Page.objects.get(permalink=pagename)
    context = {
        'title': pg.title,
        'content': pg.bodytext,
        'last_updated': pg.update_date,
        'page_list': Page.objects.all(),
    }

    return render(request, 'pages/page.html', context)
