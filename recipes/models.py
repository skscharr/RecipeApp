import datetime
from django.utils import timezone
from django.db import models

# Recipe Model
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  prep_time = models.CharField(max_length=100)
  serving_size = models.CharField(max_length=100)
  directions = models.CharField(max_length=1000000)
  pub_date = models.DateTimeField('date published')

  def __unicode__(self):
    return self.name

# Ingredient Model
class Ingredient(models.Model):
  recipe = models.ForeignKey(Recipe)
  ingredient = models.CharField(max_length=50)
  measure = models.CharField(max_length=30)

  def __unicode__(self):
    return self.ingredient