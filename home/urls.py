from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main_page.urls')),
    path('about/', include('about.urls')),
    path('contact-us/', include('contact_us.urls')),
    path('estate/', include('estate.urls')),
    path('blog/', include('blog.urls')),
    path('dashbord/', include('dashbord.urls')),
    path('', include('site_setting.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
