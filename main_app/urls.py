from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.index),
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail,name='detail'),
    # url(r'^', include(main_app.urls)),
]
