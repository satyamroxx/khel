from django.conf.urls import url, include
from django.contrib.auth import views as auth_views
from django.contrib import admin
from core import views as core_views


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^javaq/$', core_views.javaq, name='javaq'),
    url(r'^javar/$', core_views.javar, name='javar'),
    url(r'^csq/$', core_views.csq, name='csq'),
    url(r'^csr/$', core_views.csr, name='csr'),
    url(r'^cq/$', core_views.cq, name='cq'),
    url(r'^cr/$', core_views.cr, name='cr'),
    url(r'^cppq/$', core_views.cppq, name='cppq'),
    url(r'^cppr/$', core_views.cppr, name='cppr'),
    url(r'^pythonq/$', core_views.pythonq, name='pythonq'),
    url(r'^pythonr/$', core_views.pythonr, name='pythonr'),
    url(r'^mini/$', core_views.mini, name='pythonr'), 
    

    url(r'^$', core_views.home, name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),

    url(r'^logout/$', auth_views.logout, {'next_page': 'login'}, name='logout'),
    url(r'^signup/$', core_views.signup, name='signup'),
]
