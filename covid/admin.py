from django.contrib import admin

from covid.models import Contact, Subscription

admin.site.register(Subscription)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "number", "email")
    readonly_fields = ("name", "number", "email", "message")
