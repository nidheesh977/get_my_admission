from django.contrib import admin
from .models import College, CollegeCategory, CollegeImages
from django_summernote.admin import SummernoteModelAdmin

# Register your models here.
class CollegeAdmin(SummernoteModelAdmin):
    summernote_fields = ('overview', 'course_list')

admin.site.register(College, CollegeAdmin)
admin.site.register(CollegeCategory)
admin.site.register(CollegeImages)