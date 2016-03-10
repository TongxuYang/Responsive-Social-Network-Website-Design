from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', 'socialnetwork.views.home'),
    url(r'^globalstream', 'socialnetwork.views.view_the_whole'),
    url(r'^profile/(?P<username>\w+)$', 'socialnetwork.views.profile'),
    url(r'^add-item', 'socialnetwork.views.add_item'),
    url(r'^delete-item/(?P<id>\d+)$', 'socialnetwork.views.delete_item'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'socialnetwork/login.html'}),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login'),
    url(r'^register$', 'socialnetwork.views.register'),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                                    document_root=settings.STATIC_ROOT)
    
