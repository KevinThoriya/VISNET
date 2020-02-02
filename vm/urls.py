
from django.contrib import admin
from . import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('', views.index , name="main"),
    path('scanface/',views.scanface, name="scanface"),
    path('register/',views.register, name="register" ),
    path('verify/',views.verify, name="verify"), 
    path('access/',views.access, name="access"),
    path('qrscan/',views.qr,name="qrscan"),
    path('contact/',views.contact,name="contact"),
    path('about/',views.about,name="about"),
    path('verifyotp/',views.verifyotp,name="verifyotp"),
    # path('verifyotp/',views.log,name="log"),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT )
