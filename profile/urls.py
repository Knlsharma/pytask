from django.conf.urls.defaults import *

from pytask.profile.views import view_profile

urlpatterns = patterns('',

            (r'view', view_profile),
)
