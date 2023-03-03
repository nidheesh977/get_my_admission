from django.contrib import admin
from .models import Newsletter, Enquiry, ContactEnquiry

# Register your models here.
admin.site.register(Newsletter)
admin.site.register(Enquiry)
admin.site.register(ContactEnquiry)