from django.shortcuts import render
from django.views.generic import FormView

from covid.forms import ContactForm, SubscriptionForm


class SubscriptionView(FormView):
    form_class = SubscriptionForm
    success_url = '/'
    template_name = 'covid/index.html'

    def form_valid(self, form):
        form.save()
        return super(SubscriptionView, self).form_valid(form)


class ContactView(FormView):
    form_class = ContactForm
    success_url = '/'
    template_name = 'covid/contact.html'

    def form_valid(self, form):
        form.save()
        return super(ContactView, self).form_valid(form)



