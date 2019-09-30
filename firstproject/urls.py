"""firstproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from firstapp import views
from django.conf.urls import url,include

from django.conf import settings
from django.conf.urls.static import static


# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', views.index),
    url(r'^home/$',views.home),
    url(r'^user/',include('firstapp.urls')),
    url(r'^index/$',views.index2),
    url(r'^index3/$',views.index3),
    url(r'^signup/$',views.signup),
    url(r'^signup2/$',views.signup2),
    url(r'^viewdata/$',views.datafetch),
    url(r'^signup3/$',views.signup3),
    url(r'^dataup/$',views.dataupdate),
    url(r'^delete/$',views.deleteData),
    url(r'^imageviewdata/$',views.imagedatafetch),
    url(r'^imagedataup/$',views.imagedataupdate),
    url(r'^imgdelete/$',views.imgdeleteData)
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)