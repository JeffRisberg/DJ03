from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^notificationList/(?P<mode>[\w\-]+)/$', views.NotificationListView.as_view(), name='notification_list_view'),

    url(r'^notificationList/all/$', views.NotificationListView.as_view(), name='notification_list_view_all'),
    url(r'^notificationList/unread/$', views.NotificationListView.as_view(), name='notification_list_view_unread'),

    url(r'^charityList$', views.CharityListView.as_view(), name='charity_list_view'),
    url(r'^charity/(?P<slug>[\w\-]+)/$', views.CharityDetailView.as_view(), name='charity_detail_view'),
    url(r'^donorList$', views.DonorListView.as_view(), name='donor_list_view'),
    url(r'^donationList$', views.DonationListView.as_view(), name='donation_list_view'),
    url(r'^donation/(?P<id>[\w\-]+)/$', views.DonationDetailView.as_view(), name='donation_detail_view'),
    url(r'^donationNew', views.donation_new_view, name='donation_new_view'),
    url(r'^$', views.index, name='home'),
]