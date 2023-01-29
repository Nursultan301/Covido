from django.urls import path

from covid.views import ContactView, SubscriptionView

urlpatterns = [
    path('', SubscriptionView.as_view(), name='home'),
    path('contact/', ContactView.as_view(), name='contact')
]
