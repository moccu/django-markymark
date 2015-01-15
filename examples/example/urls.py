from django.conf.urls import patterns, include, url
from django.contrib import admin

from app.views import MarkdownView, PostsView


admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MarkdownView.as_view(), name='markdown'),
    url(r'^posts/$', PostsView.as_view(), name='posts'),
)
