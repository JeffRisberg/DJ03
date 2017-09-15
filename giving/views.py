from django.http.response import HttpResponse

from django.template import Context, loader

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


def new_donation_view(request):
    charity_list = Charity.objects.all()
    template = loader.get_template('giving/new_donation.html')
    context = Context({'charity_list': charity_list})
    output = template.render(context)
    return HttpResponse(output)
