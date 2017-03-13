from django.conf.urls import url
from . import views

urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    # url(r'^index/', views.index),
    url(r'^', views.index),
    # url(r'^', include(main_app.urls)),
]
