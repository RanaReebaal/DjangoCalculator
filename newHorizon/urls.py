from django.contrib import admin
from django.urls import path, include
from . import views
from django.urls import path 
from django.conf.urls.static import static
from django.conf import settings

admin.site.site_header = "New Horizon Latest Tech"
admin.site.site_title = "New Horizon Latest Tech"
admin.site.index_title = "New Horizon Latest Tech"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
    path('contact/',views.contact,name='contact'),
    path('members/',views.members,name='members'),
    path('latestTech/', include('latestTech.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

print(static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT))

