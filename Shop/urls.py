from django.contrib import admin
from django.urls import path, include
from polls import views
from polls.views import Paginator
from django.conf.urls.static import static
from django.conf import settings
from django.views.decorators.cache import cache_page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout/',views.user_logout, name='logout'),
    path('captcha/', include('captcha.urls')),
    path('__debug__/', include('debug_toolbar.urls')),
    path('cat/<int:category_id>/' ,views.get_category, name='category'),
]
if settings.DEBUG:
    import mimetypes
    mimetypes.add_type("application/javascript", ".js", True)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
