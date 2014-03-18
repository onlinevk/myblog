from django.conf.urls.defaults import patterns, include, url
from django.conf import settings
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
from django.conf.urls.static import static
from information.views import *
from users.views import *
urlpatterns = patterns('',
    # Examples:
	#url(r'^$', 'openshift.views.home', name='home'),
    # url(r'^openshift/', include('openshift.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^info$',InformationList.as_view(),name='information'),
	url(r'^$',InformationList.as_view(),name='information_list'),
	url(r'^info/(?P<pk>\d+)$',Info,name='info'),
	url(r'^new$',InformationCreate.as_view(),name='information_new'),
	url(r'^edit/(?P<pk>\d+)$',InformationUpdate.as_view(),name='information_edit'),
	url(r'^delete/(?P<pk>\d+)$',InformationDelete.as_view(),name='information_delete'),
	url(r'^like/(?P<pk>\d+)$',hitLike,name='like'),
	url(r'^clist$',CommentList.as_view(),name='comment_list'),
	url(r'^cnew$',CommentCreate.as_view(),name='comment_new'),
	url(r'^cedit/(?P<pk>\d+)$',CommentUpdate.as_view(),name='comment_edit'),
	url(r'^cdelete/(?P<pk>\d+)$',CommentDelete.as_view(),name='comment_delete'),
	url(r'^aboutus/$',aboutUs),
	url(r'^contactus/$',contactUs),
	url(r'^search/$',search),
	url(r'^preview/$',preview),

	url(r'^profile/$',ProfileList.as_view(),name='user_list'),
	url(r'^edit_profile/$',ProfileUpdate.as_view(),name='user_edit'),
	url(r'^new_profile/$',ProfileCreate.as_view(),name='user_new'),
)+static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
