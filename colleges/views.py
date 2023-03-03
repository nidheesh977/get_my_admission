from django.shortcuts import render, get_object_or_404
from .models import CollegeCategory, College, CollegeImages
# from accounts.models import SocialMedia
from django.http import Http404
from accounts.models import MetaDetails

# Create your views here.

def index(request):
    if not CollegeCategory.objects.all().exists():
        raise Http404
    categories = CollegeCategory.objects.all()
    popular_colleges = College.objects.all().order_by("-view_count")[:3]
    # if not SocialMedia.objects.all().exists():
    #     raise Http404
    # social_media = SocialMedia.objects.all()[0]
    meta_details = {}
    if MetaDetails.objects.filter(page = "homepage").exists():
      meta_details = MetaDetails.objects.get(page = "homepage")
    context = {
      "categories": categories,
      "popular_colleges": popular_colleges,
      # "social_media": social_media,
      "meta_details": meta_details
    }
    return render(request, "colleges/index.html", context = context)

def college_category_landing(request, slug):
  category = get_object_or_404(CollegeCategory, slug = slug)
  meta_details = {}
  if MetaDetails.objects.filter(page = "college_listing").exists():
    meta_details = MetaDetails.objects.get(page = "college_listing")
  context = {
    "category": category,
    "meta_details": meta_details
  }
  return render(request, "colleges/college_category_landing.html", context = context)

def college_landing(request, slug):
  college = get_object_or_404(College, slug = slug)
  college.view_count = college.view_count+1
  college.save()
  college_images = CollegeImages.objects.filter(college = college)
  meta_details = {}
  if MetaDetails.objects.filter(page = "college_landing").exists():
    meta_details = MetaDetails.objects.get(page = "college_landing")
  # if not SocialMedia.objects.all().exists():
  #       raise Http404
  # social_media = SocialMedia.objects.all()[0]
  context = {
    "college": college,
    "college_images": college_images,
    # "social_media": social_media,
    "meta_details": meta_details
  }
  return render(request, "colleges/college_landing.html", context = context)
