from django.conf.urls import patterns, url

urlpatterns = patterns('nourriture.views',
    url(r'^$', 'home'),
    # url(r'^signin$', 'signin'),
    # url(r'^signup$', 'signup'),
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
