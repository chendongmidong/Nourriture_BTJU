from django.conf.urls import patterns, url

urlpatterns = patterns('nourriture.views',
    url(r'^$', 'home'),
    url(r'^ingredient/view$', 'ingredientView'),
    url(r'^ingredient/add$', 'ingredientAdd'),
    url(r'^ingredient/delete$', 'ingredientDelete'),
    url(r'^ingredient/update$', 'ingredientUpdate'),
)
