from django.urls import path

from .views import (
    signup_view,
    post_login_view,
    login_view,
    post_signup_view
)

urlpatterns = [
    path('signup/', signup_view, name='signup'),
    path('login/', login_view, name='login'),
    path('post_login/', post_login_view, name='post_login'),
    path('post_sign_up', post_signup_view, name='post_sign_up')
]
