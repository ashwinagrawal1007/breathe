from django.conf.urls import include, url
from django.views.generic import TemplateView
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from . import views
urlpatterns = [

    url(r'^$',
        TemplateView.as_view(template_name='index.html'),
        name='index'),

    url(r'^accounts/',
        include('registration.backends.default.urls')),

    url(r'^accounts/profile/',
        TemplateView.as_view(template_name='profile.html'),
        name='profile'),

    url(r'^login/',
        'django.contrib.auth.views.login',
        name='login'),
        
    url(r'^console/',
        views.console,
        name='console'),
    
    url(r'^add_sensor/',
        views.add_sensor,
        name='add_sensor'),
        
    url(r'^delete_sensor/(?P<sensor_id>[0-9]+)/$',
        views.delete_sensor,
        name='delete_sensor'),
        
    url(r'^toggle_sensor/(?P<sensor_id>[0-9]+)/$',
        views.toggle_sensor,
        name='toggle_sensor'),
                
    url(r'^subscribe_sensor/',
        views.subscribe_sensor,
        name='subscribe_sensor'),
         
    url(r'^unsubscribe_sensor/(?P<sensor_id>[0-9]+)/$',
        views.unsubscribe_sensor,
        name='unsubscribe_sensor'),
        
    url(r'^chart/(?P<sensor_id>[0-9]+)/$',
        views.chart,
        name='chart'),  
        
    url(r'^chart_json/',
        views.chart_json,
        name='chart_json'),
        
    url(r'^admin/', include(admin.site.urls))    

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
