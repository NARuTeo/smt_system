"""server URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from potal import views as potal_views
from state_monitor import views as state_monitor_views
from service_manager import views as service_manager_views


urlpatterns = [
    #url(r'^$', potal.views.start_page , name='startpage'),
    url(r'^$',                       potal_views.start_page ,                   name='startpage'),
	url(r'^config_program/$',potal_views.config_program,   name='config_program'),

    url(r'^ws/$',                    state_monitor_views.connect_websocket,    name='connect_websocket '),
    url(r'^start_state_monitor/$',   state_monitor_views.start_state_monitor,   name='start_state_monitro'),
    url(r'^show_status/$',           state_monitor_views.show_status,           name='show_status'),
    url(r'^start_programs/$',        service_manager_views.start_programs,      name='start_programs'),
    url(r'^show_programs/$',         service_manager_views.show_programs,       name='show_programs'),
    url(r'^set_settings/$',          potal_views.modify_service_settings,       name='modify_service_settings'),
    url(r'^admin/', admin.site.urls),
    url(r'^config_program/get_config_file/$', potal_views.get_config_file,       name='get_config_file'),
    url(r'^config_program/set_config_file/$', potal_views.set_config_file,       name='set_config_file'),
    url(r'^start_server/$', service_manager_views.start_server,       name='start_server'),
    url(r'^stop_server/$', service_manager_views.stop_server,       name='stop_server')
]
