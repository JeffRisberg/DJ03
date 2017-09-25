from django.core.context_processors import csrf
from django.http.response import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import Context, loader

from notifications.signals import notify

from .models import Charity, Donor, Donation


def index(request):
    template = loader.get_template('giving/home.html')
    context = Context()
    output = template.render(context)
    return HttpResponse(output)


def charity_list_view(request):
    charity_list = Charity.objects.all()
    template = loader.get_template('giving/charity_list.html')
    context = Context({'charity_list': charity_list})
    output = template.render(context)
    return HttpResponse(output)


def donor_list_view(request):
    donor_list = Donor.objects.all()
    template = loader.get_template('giving/donor_list.html')
    context = Context({'donor_list': donor_list})
    output = template.render(context)
    return HttpResponse(output)


def donation_list_view(request):
    donation_list = Donation.objects.all()
    template = loader.get_template('giving/donation_list.html')
    context = Context({'donation_list': donation_list})
    output = template.render(context)
    return HttpResponse(output)


def donation_list_view(request):
    donation_list = Donation.objects.all()
    template = loader.get_template('giving/donation_list.html')
    context = Context({'donation_list': donation_list})
    output = template.render(context)
    return HttpResponse(output)


def new_donation_view(request):
    c = {}
    c.update(csrf(request))
    user = getattr(request, "user", None)

    if request.method == 'POST':
        notify.send(user, recipient=user, verb='Submitted donation')
        if int(request.POST['amount']) > 100:
            notify.send(user, recipient=user, verb='Big donation - send thank you email')

        id = int(request.POST['charity'])
        charity = Charity.objects.get(id__iexact=id)

        donation = Donation(donor=user, amount=int(request.POST['amount']), charity=charity)
        donation.save()
        return redirect("/giving/")

    charity_list = Charity.objects.all()
    c.update({'charity_list': charity_list})
    return render_to_response("giving/new_donation.html", c)
