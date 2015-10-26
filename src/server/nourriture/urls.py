from django.conf.urls import patterns, url, include
from rest_framework import routers
from nourriture import views

router = routers.DefaultRouter()
router.register(r'ingred', views.IngredientViewSet)
router.register(r'reci', views.RecipeViewSet)


urlpatterns = patterns('nourriture.views',
    url(r'^$', 'home'),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^ingredient/(?P<id>\d+)$', 'ingredient'),
    url(r'^ingredient/all$', 'ingredientAll'),
    url(r'^ingredient/add$', 'ingredientAdd'),
    url(r'^ingredient/delete$', 'ingredientDelete'),
    url(r'^ingredient/update$', 'ingredientUpdate'),
    url(r'^recipe/(?P<id>\d+)$', 'recipe'),
    url(r'^recipe/all$', 'recipeAll'),
    url(r'^recipe/add$', 'recipeAdd'),
    url(r'^recipe/delete$', 'recipeDelete'),
    url(r'^recipe/update$', 'recipeUpdate'),
)
