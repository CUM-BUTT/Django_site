 
"""
from django.contrib import admin
from django.urls import path
from gameportal import views

urlpatterns = [
    path('',views.index, name='home'),
    path('<int:Game_id>/',views.Games, name='Games'),
    path('sign_up/', views.sign_up, name='sign_up'),
    path('create/', views.create, name='create'),
    path('admin/', admin.site.urls),    
]"""

from django.contrib import admin 
from django.urls import path
from gameportal.views import TakeALoanView, DonateView,LoginFormView
from gameportal.views import HomeView, AboutView,RegisterFormView
from gameportal.views import LogoutView
from django.conf.urls import url
from django.conf.urls.static import static
from django.conf import settings
from gameportal import views


urlpatterns = [
    #path('', HomeView.as_view()),
    url(r'^$', HomeView.as_view()),
    #path('<int:people_id>/',views.index, name='index'),
    url(r'^About$', AboutView.as_view()),
    url(r'^TakeALoan/$', views.TakeALoan),
    url(r'^Donate/$', DonateView.as_view()),
    url('admin/', admin.site.urls), 
    url(r'^register/$', RegisterFormView.as_view()), 
    url(r'^log in/$',LoginFormView.as_view() ), 
    url(r'^log out/$',LogoutView.as_view() ), 
    path('create/', views.create, name='create'),
    #url(r'^create/$', create.as_view()),
    url(r'^update/$', views.update , name='update'),
]+ static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)

 