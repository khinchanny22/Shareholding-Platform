from django.contrib import admin

# Register your models here.
from .models import AboutUs, ContactUs, Address


class AboutUsAdmin(admin.ModelAdmin):
    list_display = ['company', 'company_info', 'mission', 'mission_description', 'vision', 'vision_description']


admin.site.register(AboutUs, AboutUsAdmin)


# contact us
class ContactUsAdmin(admin.ModelAdmin):
    list_display = ['username', 'email', 'subject', 'message']


admin.site.register(ContactUs, ContactUsAdmin)


# contact us
class AddressAdmin(admin.ModelAdmin):
    list_display = ['phone', 'email', 'fax', 'address']


admin.site.register(Address, AddressAdmin)
