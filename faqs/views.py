from django.shortcuts import render
from accounts.models import MetaDetails

# Create your views here.

def faq_list(request):
    meta_details = {}
    if MetaDetails.objects.filter(page = "faq").exists():
        meta_details = MetaDetails.objects.get(page = "faq")
    context = {
        "meta_details": meta_details
    }
    return render(request, "faqs/index.html", context=context)