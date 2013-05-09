from django.conf.urls import patterns, url
from django.views.generic import DetailView, ListView
from recipes.models import Recipe
from django.utils import timezone

urlpatterns = patterns('',
  url(r'^$',
      ListView.as_view(
          queryset=Recipe.objects.filter(pub_date__lte=timezone.now) \
          .order_by('-pub_date')[:5],
          context_object_name='all_recipes',
          template_name='recipes/index.html'),
      name='index'),
  url(r'^(?P<rk>\d+)/$',
      DetailView.as_view(
          model=Recipe,
          template_name ='recipes/detail.html'),
      name='detail'),
)