from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = patterns('',
    url(r'^$', 'socialnetwork.views.home', name='home'),
    url(r'^globalstream', 'socialnetwork.views.view_the_whole', name='globalstream'),
    url(r'^profile/(?P<username>\w+)$', 'socialnetwork.views.profile', name='profile'),
    url(r'^add-item', 'socialnetwork.views.add_item', name='add'),
    url(r'^delete-item/(?P<id>\d+)$', 'socialnetwork.views.delete_item', name='delete'),
    # Route for built-in authentication with our own custom login page
    url(r'^login$', 'django.contrib.auth.views.login', {'template_name':'socialnetwork/login.html'}, name='login'),
    # Route to logout a user and send them back to the login page
    url(r'^logout$', 'django.contrib.auth.views.logout_then_login', name='logout'),
    url(r'^register$', 'socialnetwork.views.register',name='register'),
    url(r'^profile_edit/(?P<user>\w+)$', 'socialnetwork.views.profile_edit', name='editprofile'),

)

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                                    document_root=settings.STATIC_ROOT)
    
