from django.conf.urls.defaults import *

from pytask.taskapp.views import create_task, view_task, claim_task, \
        select_user, edit_task, create_textbook

urlpatterns = patterns('',

            (r'^create/$', create_task),
            (r'^edit/tid=(\w+)$', edit_task),
            (r'^view/tid=(\w+)$', view_task),
            (r'^claim/tid=(\w+)$', claim_task),
            (r'^select/tid=(\w+)$', select_user),

            (r'^textbook/create/$', create_textbook)
)

