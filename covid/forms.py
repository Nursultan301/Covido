from django import forms
from django.utils.translation import ugettext_lazy as _


from covid.models import Contact, Subscription


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

        widgets = {
            "name": forms.TextInput(attrs={'class': 'contactus', 'placeholder': _('Имя')}),
            "number": forms.TextInput(attrs={'class': 'contactus', 'placeholder': _('Телефон номер')}),
            "email": forms.EmailInput(attrs={'class': 'contactus', 'placeholder': 'Email'}),
            "message": forms.Textarea(attrs={'class': 'textarea', 'rows': 8, 'placeholder': _('Сообщение')}),
        }


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = ('email',)

        widgets = {
            "email": forms.EmailInput(attrs={'class': 'newsl', 'placeholder': 'Ваш адрес электронной почты'}),
        }
