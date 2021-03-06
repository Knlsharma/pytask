#!/usr/bin/env python
#
# Copyright 2011 Authors of PyTask.
#
# This file is part of PyTask.
#
# PyTask is free software: you can redistribute it and/or modify it
# under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# PyTask is distributed in the hope that it will be useful, but WITHOUT
# ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or
# FITNESS FOR A PARTICULAR PURPOSE. See the GNU General Public License
# for more details.
#
# You should have received a copy of the GNU General Public License
# along with PyTask.  If not, see <http://www.gnu.org/licenses/>.


__authors__ = [
    '"Madhusudan.C.S" <madhusudancs@fossee.in>',
    '"Nishanth Amuluru" <nishanth@fossee.in>',
    ]


from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url


urlpatterns = patterns('pytask.taskapp.views.task',
  url(r'^create/$', 'create_task', name='create_task'),
  url(r'^edit/(?P<task_id>\d+)$', 'edit_task', name='edit_task'),
  url(r'^view/(?P<task_id>\d+)$', 'view_task', name='view_task'),
  url(r'^claim/(?P<task_id>\d+)$', 'claim_task', name='claim_task'),
  url(r'^select/(?P<task_id>\d+)$', 'select_user', name='select_user'),
  url(r'^approve/(?P<task_id>\d+)$', 'approve_task',
      name='approve_task'),
  url(r'^approved/(?P<task_id>\d+)$', 'approved_task',
      name='approved_task'),
  url(r'^addreviewer/(?P<task_id>\d+)$', 'addreviewer',
      name='addreviewer_task'),
  url(r'^view/work/(?P<task_id>\d+)$', 'view_work', name='view_work'),
  url(r'^view/report/(?P<report_id>\d+)$', 'view_report',
      name='view_report'),
  url(r'^submit/report/(?P<task_id>\d+)$', 'submit_report',
      name='submit_report'),
  url(r'^browse/$', 'browse_tasks', name='browse_tasks'),
)

# URL patterns specific to textbook projects.
urlpatterns += patterns('pytask.taskapp.views.textbook',
  url(r'^textbook/create/$', 'create_textbook',
      name='create_textbook'),
  url(r'^textbook/view/(?P<task_id>\d+)$', 'view_textbook',
      name='view_textbook'),
  url(r'^textbook/edit/(?P<task_id>\d+)$', 'edit_textbook',
      name='edit_textbook'),
  url(r'^textbook/approve/(?P<task_id>\d+)$', 'approve_textbook',
      name='approve_textbook'),
  url(r'^textbook/approved/(?P<task_id>\d+)$', 'approved_textbook',
      name='approved_textbook'),
  url(r'^textbook/browse/$', 'browse_textbooks',
      name='browse_textbooks'),
  url(r'^textbook/chapter/create/(?P<book_id>\d+)$', 'create_chapter',
      name='create_chapter'),
  url(r'^textbook/chapter/edit/(?P<book_id>\d+)/(?P<chapter_id>\d+)$',
      'edit_chapter',
      name='edit_chapter'),
  url(r'^textbook/chapter/view/(?P<book_id>\d+)/(?P<chapter_id>\d+)$',
      'view_chapter',
      name='view_chapter'),
)

# URL patterns specific to tags.
urlpatterns += patterns('pytask.taskapp.views.task',
  url(r'^tag/suggest/$', 'suggest_task_tags', name='suggest_task_tags'),
  url(r'^tag/view/(?P<tag_name>[\w\-&./\'\" ]+)$', 'view_tag', name='view_tag'),
)
