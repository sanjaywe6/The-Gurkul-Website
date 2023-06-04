"""thegurkul URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include

admin.site.site_header = "The Gurkul Admin"
admin.site.site_title = "The Gurkul Portal"
admin.site.index_title = "Designed, Developed and Managed by Mr. Sanjay Gupta ( Co-Director and Founder of The Gurkul )"

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home,name="Home"),
    
    path('total_visitor/', views.total_visitor,name="Total visitor data function"),

    path('about/', views.about,name="About"),

    path('contact/', views.contact,name="contact"),

    path('user/profile',views.user_profile,name='handling go to profile'),

    path('user_registration/', views.usrRegistration,name='User Registration Page'),

    path('user_login/',views.usrLogin,name="User Login Form"),

    path('user_logout/',views.usrLogout,name="User Logout Form"),

    path('gurkul_student/',include('gurkul_student.urls')),

    path('gurkul_teacher/',include('gurkul_teacher.urls')),

    path('gurkul_branch/',include('gurkul_branch.urls')),

    path('gurkul_administration/',include('gurkul_admin.urls')),

    path('gurkul_test/',include('gurkul_test.urls')),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
