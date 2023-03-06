from django.urls import path
from .views import home
from .views import RecipeListView
from .views import RecipeDetailView
from .views import records

app_name = 'recipes'

urlpatterns = [
    path('', home),
    path('list/', RecipeListView.as_view(), name='list'),
    path('list/<pk>', RecipeDetailView.as_view(), name='details'),
    path('search/', records, name='search'),
]
