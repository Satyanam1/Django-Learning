"""
URL configuration for project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from app import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),

    path('contact/',views.contact,name='contact'),
    path('contact_data/',views.contact_data,name='contact_data'),

    path('register/',views.register,name='register'),
    path('regis/',views.regis,name='regis'),

    path('login/',views.login_view,name='login'),
    path('login_data/',views.login_data,name='login_data'),

    path('logout/',views.logout_user,name='logout'),


    # path('dashboard/<int:x>/',views.dashboard,name='dashboard'), 
    path('dashboard/',views.dashboard,name='dashboard'), 

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


