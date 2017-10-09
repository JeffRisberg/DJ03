from django.core.context_processors import csrf
from django.http.response import HttpResponse
from django.shortcuts import redirect, render_to_response
from django.template import Context, loader
from django.views.generic import TemplateView, ListView

from notifications.models import Notification
from notifications.signals import notify

from .models import Charity, Donor, Donation


def index(request):
    template = loader.get_template('giving/home.html')
    context = Context()
    output = template.render(context)
    return HttpResponse(output)


class NotificationListView(ListView):
    template_name = 'giving/notification_list.html'
    model = Notification

    def get_queryset(self):
        mode = self.kwargs['mode'] or 'all'
        if mode == 'unread':
            return self.request.user.notifications.unread()
        elif mode == 'read':
            return self.request.user.notifications.read()
        else:
            return self.request.user.notifications.all()

    def get_context_data(self, **kwargs):
        context = super(NotificationListView, self).get_context_data(**kwargs)
        mode = self.kwargs['mode'] or 'all'
        context['mode'] = mode
        return context


class CharityListView(ListView):
    model = Charity


class CharityDetailView(TemplateView):
    template_name = 'giving/charity_detail.html'

    def get_context_data(self, **kwargs):
        return {'charity': Charity.objects.get(slug__iexact=kwargs['slug'])}


class DonorListView(ListView):
    model = Donor


class DonationListView(ListView):
    model = Donation


class DonationDetailView(TemplateView):
    template_name = 'giving/donation_detail.html'

    def get_context_data(self, **kwargs):
        return {'donation': Donation.objects.get(id=kwargs['id'])}


def donation_new_view(request):
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
    else:
        notify.send(user, recipient=user, verb='Started creation of donation')

    charity_list = Charity.objects.all()
    c.update({'charity_list': charity_list})
    return render_to_response("giving/donation_new.html", c)
