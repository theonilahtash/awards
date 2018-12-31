from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^search/',views.search_results,name='search_results'),
    # url(r'^profile/(\d+)',views.profile,name = 'profile'),
    url(r'^new/profile$',views.add_profile,name='add_profile'),
    url(r'^new/project$', views.new_project, name='new-project'),
    url(r'^review/(?P<pk>\d+)',views.add_review,name='review'),
    url(r'^api/profile$',views.ProfileList.as_view()),
    url(r'^api/projects$',views.ProjectList.as_view()),

]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
