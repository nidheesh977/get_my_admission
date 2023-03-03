from django import template
# from accounts.models import SocialMedia
from colleges.models import College, CollegeCategory
from django.http import Http404

register = template.Library()

# @register.simple_tag
# def get_social_media():
#     if not SocialMedia.objects.all().exists():
#         raise Http404
#     social_media = SocialMedia.objects.all()[0]
#     return social_media

@register.simple_tag
def get_popular_five_colleges():
    colleges = College.objects.all().order_by("-view_count")[:5]
    return colleges

@register.simple_tag
def get_all_categories():
    if not CollegeCategory.objects.all().exists():
        raise Http404
    categories = CollegeCategory.objects.all()
    return categories