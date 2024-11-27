# intranet_server/urls.py
from django.contrib import admin
from django.urls import path, include
from accounts import views as accounts_views
from worklog import views as worklog_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', accounts_views.signup_view, name='signup'),
    path('login/', accounts_views.login_view, name='login'),
    path('worklog/', worklog_views.worklog_menu, name='worklog_menu'),
]
