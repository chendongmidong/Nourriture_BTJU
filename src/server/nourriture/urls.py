from django.conf.urls import patterns, url

urlpatterns = patterns('nourriture.views',
    url(r'^$', 'home'),
    url(r'^ingredient/view$', 'ingredientView'),
)
