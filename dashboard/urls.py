from django.urls import path,include
from . import views
from django.conf import settings 
from  django.conf.urls.static import static

app_name='admindashboard'

urlpatterns = [
    path('index/',views.index,name='index'),
    path('',views.loginpage,name='login'),
    path('register/',views.register,name='register'),
    path('discountcode/',views.discountcode,name='discountcode'),
    path('docs/',views.docs,name='docs'),
    path('icontabler/',views.icontabler,name='icontabler'),
    path('samplepage/',views.samplepage,name='samplepage'),
    path('alerts/',views.alerts,name='alerts'),
    path('buttons/',views.buttons,name='buttons'),
    path('card/',views.card,name='card'),
    path('forms/',views.forms,name='forms'),
    path('typography/',views.typography,name='typography'),

    path('registersave/',views.registersave,name='registersave'),
    path('loginsave/',views.loginsave,name='loginsave'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)