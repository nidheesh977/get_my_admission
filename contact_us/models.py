from django.db import models

# Create your models here.
    
class Newsletter(models.Model):
    email = models.EmailField(max_length = 200, unique = True)

    def __str__(self):
        return self.email
    
class Enquiry(models.Model):
  name = models.CharField(max_length = 200)
  phone = models.CharField(max_length = 14)
  email = models.EmailField()
  message = models.TextField()
  url = models.URLField()

  def __str__(self):
    return self.name
    
class ContactEnquiry(models.Model):
  name = models.CharField(max_length = 200)
  phone = models.CharField(max_length = 14)
  email = models.EmailField()
  message = models.TextField()

  def __str__(self):
    return self.name