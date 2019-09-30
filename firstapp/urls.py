from firstapp import views
from django.conf.urls import url

app_name = 'firstapp'
urlpatterns = [
    url(r'^about/$',views.about,name="about1")


]