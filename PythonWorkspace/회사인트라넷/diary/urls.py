from django.urls import path
from .views import signup, login_view, home, add_entry

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('', home, name='home'),
    path('add/', add_entry, name='add_entry'),
]
