from django.conf import settings
from django.urls import path
from . import views
from . import views_auth
from django.conf.urls.static import static


urlpatterns = [
    path('', views.bio, name='bio'),
    path('register/', views_auth.reg, name='reg'),
    path('login/', views_auth.log, name='log'),
    path('account', views_auth.acc, name='acc'),
    path('account/courses', views.courses, name='courses'),
    path('account/courses/<int:course_id>/', views.course_detail, name='course_detail'),
    path('account/courses/<int:course_id>/lessons/<int:lessons_id>/', views.lessons_detail, name='lessons_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)