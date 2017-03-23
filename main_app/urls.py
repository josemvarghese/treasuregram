from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.index),
    url(r'^$', views.index, name='index'),
    url(r'^([0-9]+)/$', views.detail,name='detail'),
    url(r'^post_url/$', views.post_treasure, name="post_treasure"),
    url(r'^delete_treasure/([0-9]+)/$', views.delete_treasure, name="delete_treasure"),
    url(r'^user/(\w+)/$', views.profile, name="profile"),
    url(r'^login/$', views.login_view, name="login"),
]
