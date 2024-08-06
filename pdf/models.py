from django.db import models

class PDFFilebe(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/be/')

    def __str__(self):
        return self.title
    
class PDFFilebme(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/bme/')

    def __str__(self):
        return self.title
class PDFFilechem(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/chem/')

    def __str__(self):
        return self.title
class PDFFilemaths(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/maths/')

    def __str__(self):
        return self.title
class PDFFilemos(models.Model):
    title = models.CharField(max_length=100)
    pdf = models.FileField(upload_to='pdfs/mos/')

    def __str__(self):
        return self.title

# models.py
from django.contrib.auth.models import User
from django.db import models


class UserPoints(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    points = models.IntegerField(default=0)

    def __str__(self):
        return f"Points for {self.user.username}"
    
    from django.db import models

    from django.db import models

class Reward(models.Model):
    name = models.CharField(max_length=100)
    points_required = models.PositiveIntegerField()

    def __str__(self):
        return self.name

