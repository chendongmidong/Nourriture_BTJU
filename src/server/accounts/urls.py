from django.conf.urls import patterns, url

urlpatterns = patterns('accounts.views',
    # url(r'^$', 'home'),
    url(r'^signup$', 'signup'),
    url(r'^login$', 'login'),
)
