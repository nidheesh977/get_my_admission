from django.db import models

# Create your models here.

class College(models.Model):
  name = models.CharField(max_length = 200, unique = True)
  slug = models.SlugField(unique = True)
  location = models.CharField(max_length = 200)
  image = models.ImageField(upload_to = "images/college", help_text="Select image of size 510x300")
  logo = models.ImageField(upload_to = "images/college/logos", help_text="Select image of size 75x75")
  brochure = models.FileField(upload_to='documents/brochure')
  approved_by = models.CharField(max_length = 200)
  view_count = models.IntegerField(default = 0)
  course_offered = models.IntegerField()
  total_faculty = models.IntegerField()
  established_in = models.DateField()
  max_package = models.CharField(max_length = 200)
  fee_range = models.CharField(max_length = 200)
  college_type = models.CharField(max_length = 200, default = "Public")
  NIRF_Ranking = models.IntegerField()
  short_description = models.TextField()
  reviews_count = models.IntegerField()
  rating = models.IntegerField()
  overview = models.TextField()
  course_list = models.TextField()

  def __str__(self):
    return self.name

class CollegeCategory(models.Model):
  name = models.CharField(max_length = 200, unique = True)
  slug = models.SlugField(unique = True)
  # image = models.ImageField(upload_to = "images/collegeCategory")
  colleges = models.ManyToManyField(College, blank = True)

  def __str__(self):
    return self.name


class CollegeImages(models.Model):
  image = models.ImageField(upload_to = "images/collegeImages", help_text="Select image of size 280x175")
  college = models.ForeignKey(College, on_delete=models.CASCADE)

  def __str__(self):
    return self.college.name