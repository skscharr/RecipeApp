from django.contrib import admin
from recipes.models import Recipe, Ingredient

class IngredientInline(admin.TabularInline):
  model = Ingredient
  extra = 5

class RecipeAdmin(admin.ModelAdmin):
  fieldsets = [
    (None, {'fields': ['name']}),
    ('Date', {'fields': ['pub_date']}),
    ('Directions', {'fields': ['directions']}),
  ]
  inlines = [IngredientInline]
  search_fields = ['name', 'ingredient']
  list_display = ('name', 'pub_date')
  list_filter = ['pub_date']
  date_hierarchy = 'pub_date'

admin.site.register(Recipe, RecipeAdmin)