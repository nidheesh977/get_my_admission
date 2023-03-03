from django.shortcuts import render
# from accounts.models import SocialMedia
from django.http import Http404, JsonResponse, HttpResponse
from .models import Newsletter
from .form import EnquiryForm,  ContactEnquiryForm
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail, EmailMultiAlternatives
from accounts.models import MetaDetails
from django.template.loader import get_template
from django.template import Context

# Create your views here.
def contact(request):
  # social_media = SocialMedia.objects.all()[0]
  meta_details = {}
  if MetaDetails.objects.filter(page = "contact").exists():
      meta_details = MetaDetails.objects.get(page = "contact")
  context = {
    # "social_media": social_media,
    "meta_details": meta_details
  }
  return render(request, "contact_us/contact.html", context = context)

def newsletter(request):
  if request.method == "POST":
    if request.POST.get("email"):
      if Newsletter.objects.filter(email = request.POST.get("email")).exists():
        return JsonResponse({"message":"Email ID already exists"}, status = 400)
      Newsletter.objects.create(email = request.POST.get("email"))
      return JsonResponse({"response":"Subscription added successfully"}, status = 200)
    else:
      return JsonResponse({"message":"Email ID not given"}, status = 400)
  return Http404

def enquiryFormSubmit(request):
  if request.method == "POST":
    form = EnquiryForm(request.POST)
    if form.is_valid():
      # print(form.data)
      form.save()
      subject = f'{form.data["name"]} - New enquiry'
      email_from = settings.EMAIL_HOST_USER
      email_admin = settings.EMAIL_ADMIN
      recipient_list = [email_admin, "nidheesh.nexevo@gmail.com"]
      plaintext = get_template('contact_us/email_template.txt')
      htmly     = get_template('contact_us/email_template.html')

      d = { 
        'name': form.data["name"],
        'email': form.data['email'],
        'phone': form.data["phone"],
        'url': form.data["url"],
        'message': form.data["message"]
      }

      text_content = plaintext.render(d)
      html_content = htmly.render(d)
      msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
      msg.attach_alternative(html_content, "text/html")
      msg.send()

      return JsonResponse({"response":"Enquired successfully"}, status = 200)
    else:
      print(form.errors)
      return JsonResponse(form.errors, status = 400)
  return Http404

def contactEnquiryFormSubmit(request):
  if request.method == "POST":
    form = ContactEnquiryForm(request.POST)
    if form.is_valid():
      # print(form.data)
      form.save()
      subject = f'{form.data["name"]} - New contact enquiry'
      email_from = settings.EMAIL_HOST_USER
      email_admin = settings.EMAIL_ADMIN
      recipient_list = [email_admin, "nidheesh.nexevo@gmail.com"]
      plaintext = get_template('contact_us/email_contact_template.txt')
      htmly     = get_template('contact_us/email_contact_template.html')

      d = { 
        'name': form.data["name"],
        'email': form.data['email'],
        'phone': form.data["phone"],
        'message': form.data["message"]
      }

      text_content = plaintext.render(d)
      html_content = htmly.render(d)
      msg = EmailMultiAlternatives(subject, text_content, email_from, recipient_list)
      msg.attach_alternative(html_content, "text/html")
      msg.send()
      return JsonResponse({"response":"Enquired successfully"}, status = 200)
    else:
      print(form.errors)
      return JsonResponse(form.errors, status = 400)
  return Http404