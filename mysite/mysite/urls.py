"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from Activities import views
from ActivityNews.views import index, finspeact, latestnews, workshopnews
from DepartIntro.views import departintro, teachgoal, legislation, equipment, offregulation
from RecruStu.views import sportexcellent, senioradmi, unitestdistribute, transform, masteradmission, manightadmission, liston, trafficmethod
from Teacher.views import fulltime_teacher, fulldetail, parttime_teacher, partdetail
from University.views import courseplan, curriculum, studentcorner, crossdomain
from Master.views import teachmaster, coursearchi, bachelortest, seminar, schoolpaper, graduatedpaper, studygroup , archeology
from Masternight.views import ncoursearchi
from Others.views import honor, alumni, stuaccociation, coursemap
from Activities.views import activities1, actdetail, activities2, activities3
from SportMagzine.views import sportmagzine

admin.autodiscover()

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^latestnews/', latestnews),
    url(r'^workshopnews/', workshopnews),
    url(r'^depart_character/', departintro),
    url(r'^$', index),
    url(r'^crossdomain/', crossdomain),
    url(r'^teachmaster/', teachmaster),
    url(r'^teachgoal/', teachgoal),
    url(r'^finspeact/(?P<id>\d+)/$', finspeact),
    url(r'^legistlate/', legislation),
    url(r'^equipment/', equipment),
    url(r'^offregulation/', offregulation),
    url(r'^sportexcellent/', sportexcellent),
    url(r'^senioradmi/', senioradmi),
    url(r'^unitestdistribute/', unitestdistribute),
    url(r'^fullteacher/', fulltime_teacher),
    url(r'^partteacher/', parttime_teacher),
    url(r'^transform/', transform),
    url(r'^masteradmission/', masteradmission),
    url(r'^manightadmission/', manightadmission),
    url(r'^liston/', liston),
    url(r'^trafficmethod/', trafficmethod),
    url(r'^courseplan/', courseplan),
    url(r'^curriculum/', curriculum),
    url(r'^studentcorner/', studentcorner),
    url(r'^coursearchi/', coursearchi),
    url(r'^bachelortest/', bachelortest),
    url(r'^seminar/', seminar),
    url(r'^schoolpaper/', schoolpaper),
    url(r'^graduatedpaper/', graduatedpaper),
    url(r'^studygroup/', studygroup),
    url(r'^ncoursearchi/', ncoursearchi),
    url(r'^honor/', honor),
    url(r'^alumni/', alumni),
    url(r'^stuaccociation/', stuaccociation),
    url(r'^coursemap/', coursemap),
    url(r'^fulldetail/(?P<id>\d+)/$', fulldetail),
    url(r'^partdetail/(?P<id>\d+)/$', partdetail),
    url(r'^actdetail/(?P<id>\d+)/$', actdetail),
    url(r'^activities1/', activities1),
    url(r'^activities2/', activities2),
    url(r'^activities3/', activities3),
    url(r'^sportmagzine/', sportmagzine),
    url(r'^archeology/', archeology),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
