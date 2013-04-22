from django.db import models

MEASURE_TYPES = (
  ('tbsp', 'tablespoon'), 
  ('tsp', 'teaspoon'),
  ('C', 'cup'),
  ('pt', 'pint'),
  ('qt', 'quart'),
  ('gal', 'gallon'),
  ('fl oz', 'fluid ounce'), 
  ('oz', 'ounce')
)

# Create your models here.
class Recipe(models.Model):
  name = models.CharField(max_length=100)
  ingredient = models.CharField()
  measure = models.IntegerField('measurement')
  measure_type = models.CharField('measurement type', max_length=5, choices=MEASURE_TYPES)
  directions = models.CharField()

  def __unicode__(self):
    return self.name