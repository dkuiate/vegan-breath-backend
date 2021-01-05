from django.db import models

# Create your models here.

class Contact(models.Model):
  email = models.EmailField(max_length=100)
  name = models.CharField(max_length=200)

class Recette(models.Model):
  title = models.CharField(max_length=200, unique=True)
  description = models.TextField()
  picture = models.ImageField(upload_to = 'recettes')
  created_at= models.DateTimeField(auto_now_add=True)
  def __str__(self):
        return self.title


class Restaurant(models.Model):
  title = models.CharField(max_length=200, unique=True)
  email = models.EmailField(max_length=100)
  description = models.TextField()
  created_at= models.DateTimeField(auto_now_add=True)
  picture = models.URLField(max_length=200)
  #picture = models.ImageField(upload_to = 'restaurants')
  def __str__(self):
        return self.title


class Shop(models.Model):
  title = models.CharField(max_length=200, unique=True)
  description = models.TextField()
  email = models.EmailField(max_length=100)
  created_at= models.DateTimeField(auto_now_add=True)
  picture = models.URLField(max_length=200)
  def __str__(self):
        return self.title



