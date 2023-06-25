from django.urls import path
from .views import home_page, post_data

urlpatterns = [
    path('', home_page, name='home'),
    path('data', post_data, name='post_data')
]
