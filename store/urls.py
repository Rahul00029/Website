from django.contrib import admin
from django.urls import path
from store import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path("",views.index,name='index'),
    path("loginuser",views.loginuser,name='loginuser'),
    path("logoutuser",views.logoutuser,name='logoutuser'),
    path("signup",views.signup,name="signup"),
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

