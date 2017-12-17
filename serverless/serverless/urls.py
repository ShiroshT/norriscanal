from django.conf.urls import  include, url
from django.contrib import admin
from boards import views

urlpatterns = [
    url(r'^', include('boards.urls')),
    url(r'^admin/', admin.site.urls),
]

# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^boards/', include('boards.urls')),
# ] 