from django.urls import path
from . import views

urlpatterns = [
  path("", views.contact, name = "contact"),
  path("newsletter/", views.newsletter, name = "newsletter"),
  path("enquiry/", views.enquiryFormSubmit, name = "enquiry"),
  path("contact-enquiry/", views.contactEnquiryFormSubmit, name = "contact-enquiry"),
]

