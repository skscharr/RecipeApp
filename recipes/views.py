from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

from recipes.models import Recipe, Ingredient

# view existing recipe
def recipe(request, template='recipes/detail.html'):
  r = get_object_or_404(Recipe, rk=recipe_id)
  this_recipe = Recipe.objects.get(id=request.GET['recipe_id'])

  return render(request, template, {
    'recipe': r,
    'error_message': "Error",
  })

# create a new recipe
def create_recipe(request, template='recipes/new_recipe.html'):
  recipe_title = request.POST['title'] # request.POST is a dict that comes from your form; the keys of request.POST will come from the name attribute of your HTML <input> element
  recipe_directions = request.POST['directions']
  recipe_ingredients = reqeust.POST['ingredient']
    
  new_recipe = Recipe(title=recipe_title, directions=recipe_directions, content=recipe_ingredients)
  new_recipe.save() #https://docs.djangoproject.com/en/dev/topics/db/queries/#creating-objects
    
  return render(request, template)

# deleting a recipe
def delete_recipe(request, template='recipes/recipe_delete.html'):
  this_recipe = Recipe.objects.get(id=request.POST['recipe_id']) # https://docs.djangoproject.com/en/dev/topics/db/queries/#retrieving-objects
  this_recipe.delete() # https://docs.djangoproject.com/en/dev/topics/db/queries/#deleting-objects
 
  return render(request, template)

# updating a recipe
def update_recipe(request, template='recipes/successful_update.html'):
  this_recipe = Recipe.objects.get(name=request.POST['recipe_name'] # https://docs.djangoproject.com/en/dev/topics/db/queries/#retrieving-a-single-object-with-get
  this_recipe.directions = request.POST['directions']
  this_recipe.ingredient = request.POST['ingredient']
  this_recipe.save()

  return render(request, template)